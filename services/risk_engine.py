import joblib
import numpy as np
from pathlib import Path
from typing import Optional

#-------Model paths-------

BASE_DIR = Path(__file__).parent.parent

MODEL_PATH = BASE_DIR / "notebooks" / "ml_models" / "risk_model.joblib"
SCALER_PATH = BASE_DIR / "notebooks" / "ml_models" / "scaler.joblib"

#-------Load once at module import time--------
#This runs when FastAPI starts - not on every request

try:
    _model = joblib.load(MODEL_PATH)
    _scaler= joblib.load(SCALER_PATH)
    print("Risk model loaded successfilly")
except FileNotFoundError:
    _model = None
    _scaler= None
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

def predict(
        glucose:          Optional[float] = None,
        blood_pressure:   Optional[float] = None,
        bmi:              Optional[float] = None,
        age:              Optional[float] = None,
)-> dict:
    """Run risk prediction. Missing values use dataset median"""

    if _model is None:
        return{
            "risk_score":      0.0,
            "level":           "unavailable",
            "top_factor":      [],
            "used_defaults":   True

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
    features  = np.array([[g, bp, b, a]])
    scaled   = _scaler.transform(features)
    score    = float(_model.predict_proba(scaled)[0][1])
    level    = get_risk_level(score)

    #Build human- readable top factors
    top_factors = []
    if g  > 140: top_factors.append("elevated glucose")
    if b  > 30:  top_factors.append("high BMI")
    if a  > 45:  top_factors.append("age factor")
    if bp > 80:  top_factors.append("elevated blood pressure")
    if not top_factors:
        top_factors = ["values within normal range"]

    return {
        "risk_score":   round(score, 3),
        "level":        level,
        "top_factors":  top_factors,
        "used_defaults": len(missing) > 0,
        "missing_fields": missing
    }

