import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


#----Step 1 : Load dataset -------
df = pd.read_csv("notebook/dataset/diabetes.csv")
print(df.head())

#----Step 2 : Load dataset------
FEATURES=["Glucose", "BloodPressure","BMI","Age"]
TARGET = "Outcome"

X = df[FEATURES]
y = df[TARGET]

#----Step 3 : Handle zeros(invalid medical values)-----
#In this dataset, 0 means missing data - replace with median
for col in ["Glucose","BloodPressure","BMI"]:
    X[col] = X[col].replace(0, X[col].median())

print(f"\nFeature stats after cleaning:")
print(X.describe())

#----Step 4 : Split data ------
X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTrain: {len(X_train)}, Test: {len(X_test)}")

# ── Step 5: Scale features ────────────────────────────
scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ── Step 6: Train model ───────────────────────────────
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=6,
    random_state=42,
    class_weight="balanced"   # handles imbalanced classes
)
model.fit(X_train, y_train)

# ── Step 7: Evaluate ──────────────────────────────────
y_pred   = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ── Step 8: Feature importance ────────────────────────
importances = dict(zip(FEATURES, model.feature_importances_))
print("\nFeature importances:")
for feat, imp in sorted(importances.items(), key=lambda x: -x[1]):
    print(f"  {feat}: {imp:.3f}")

# ── Step 9: Save model and scaler ─────────────────────
os.makedirs("ml_models", exist_ok=True)
joblib.dump(model,  "ml_models/risk_model.joblib")
joblib.dump(scaler, "ml_models/scaler.joblib")
print("\n✓ Model saved to ml_models/risk_model.joblib")
print("✓ Scaler saved to ml_models/scaler.joblib")

# ── Step 10: Test prediction on a sample ─────────────
sample = np.array([[120, 70, 25.0, 25]])  # glucose, bp, bmi, age
sample_scaled  = scaler.transform(sample)
risk_prob      = model.predict_proba(sample_scaled)[0][1]
print(f"\nSample prediction:")
print(f"  Input:      glucose=120, bp=70, bmi=25.0, age=25")
print(f"  Risk score: {risk_prob:.3f}")
print(f"  Level:      {'high' if risk_prob > 0.6 else 'medium' if risk_prob > 0.3 else 'low'}")
