import joblib
import numpy as np
from pathlib import Path
from typing import Optional
import shap

#-------Model paths-------

BASE_DIR = Path(__file__).parent.parent

MODEL_PATH = BASE_DIR / "notebooks" / "ml_models" / "risk_model.joblib"
SCALER_PATH = BASE_DIR / "notebooks" / "ml_models" / "scaler.joblib"

FEATURES = ["glucose", "blood_pressure","bmi","age"]

#-------Load once at module import time--------
#This runs when FastAPI starts - not on every request

try:
    _model = joblib.load(MODEL_PATH)
    _scaler= joblib.load(SCALER_PATH)
    _explainer = shap.TreeExplainer(_model)

    print("Risk model loaded successfilly")
except FileNotFoundError:
    _model = None
    _scaler= None
    _explainer = None
    print("Risk model not found - run notebooks/train_model.py first")

#--------Default value when user hasn't provided a field
DEFAULTS = {
    "glucose":          117.0,       #dataset median
    "blood_pressure":   72.0,
    "bmi":              32.0,
    "age":              33.0
}


def get_risk_level(score: float) -> str:
    if score >= 0.6 :
        return "high"
    elif score >= 0.3: 
        return "medium"
    return "low"

#------SHAP Explanation-------
def _build_shap_explanation(shap_vals:dict) ->str:
    """Turn SHAP values into human- readable sentence."""
    #Sort by absolute impact, Biggest risk first

    
    positive_vals ={
        k: v for k, v in shap_vals.items()
        if v > 0
    }

    if positive_vals:
        top_feature = max(positive_vals, key= positive_vals.get)
        top_val = positive_vals[top_feature]
    
    else:
        top_feature, top_val = sorted(
            shap_vals.items(),
            key= lambda x: abs(x[1]),
            reverse= True
        )[0]

    advice = {
        "glucose":          "Consider reducing sugar and refined carb intake.",
        "bmi":              "Regular exercise  and a balance dite can help.",
        "age":              "Age is a factor -  regular checkups are important.",
        "blood_pressure":   "Monitor your blood pressure regularly."
}

    direction = "increasing" if top_val > 0 else "decreasing"
    tip = advice.get(top_feature,"Consult a healthcare professional")

    return (
        f"{top_feature.replace('_',' ').title()} is your biggest risk driver "
        f"({direction} risk by {abs(top_val):.2f}). {tip}"
    )
#------Predict function -------

def predict(
        glucose:          Optional[float] = None,
        blood_pressure:   Optional[float] = None,
        bmi:              Optional[float] = None,
        age:              Optional[float] = None,
)-> dict:
    """Run risk prediction. Missing values use dataset median"""

    if _model is None:
        return {
    "risk_score": 0.0,
    "level": "unavailable",
    "top_factors": [],
    "shap_explanation": {},
    "explanation": "Model unavailable",
    "used_defaults": True,
    "missing_fields": []
}
    
    #Use provided values or fall back to defaults

    g = glucose            if glucose           is not None else DEFAULTS["glucose"]
    bp=blood_pressure      if blood_pressure    is not None else DEFAULTS["blood_pressure"]
    b =bmi                 if bmi               is not None else DEFAULTS["bmi"]
    a =age                 if age               is not None else DEFAULTS["age"]

    #Track which fields are missing
    missing = []
    if glucose            is None: missing.append("glucose")
    if blood_pressure     is None: missing.append("blood_pressure")
    if bmi                is None: missing.append("bmi")
    if age                is None: missing.append("age")

    #Bulid features array -  order must match  training: glucose, bp, bmi, age
    print("INPUT VALUES")
    print("glucose =", g)
    print("blood_pressure =", bp)
    print("bmi =", b)
    print("age =", a)

    features  = np.array([[g, bp, b, a]])
    print("FEATURE VECTOR =", features)
    scaled   = _scaler.transform(features)
    score    = float(_model.predict_proba(scaled)[0][1])
    level    = get_risk_level(score)


        # ----- SHAP values -----

    print("Reached SHAP section")

    try:
        shap_values = _explainer.shap_values(scaled)

        print("SHAP TYPE:", type(shap_values))

        if isinstance(shap_values, list):
            shap_arr = np.array(shap_values[1][0])

        else:
            shap_arr = np.array(shap_values)

            print("SHAP SHAPE:", shap_arr.shape)

            if shap_arr.ndim == 3:
                shap_arr = shap_arr[0, :, 1]

            elif shap_arr.ndim == 2:
                shap_arr = shap_arr[0]

        shap_arr = np.ravel(shap_arr)

        print("FINAL SHAP ARRAY:", shap_arr)

        shap_dict = {
            feat: round(float(val), 4)
            for feat, val in zip(FEATURES, shap_arr)
        }

    except Exception as e:
        print("SHAP ERROR:", e)

        shap_dict = {
            "glucose": 0.0,
            "blood_pressure": 0.0,
            "bmi": 0.0,
            "age": 0.0
        }

    top_factors = [
        f for f, v in
        sorted(shap_dict.items(), key=lambda x: -x[1])
        if v > 0
    ]

    if not top_factors:
        top_factors = ["all values within normal range"]

    explanation = _build_shap_explanation(shap_dict)

    if missing:
        explanation += (
            f" (Note: {', '.join(missing)} used population averages.)"
        )

    return {
        "risk_score": round(score, 3),
        "level": level,
        "top_factors": top_factors,
        "shap_explanation": shap_dict,
        "explanation": explanation,
        "used_defaults": len(missing) > 0,
        "missing_fields": missing
    }