import pandas as pd
import numpy as np
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# ── Step 1: Load Dataset ──────────────────────────────
df = pd.read_csv("notebooks/dataset/diabetes.csv")

print("\nDataset Preview:")
print(df.head())


# ── Step 2: Select Features & Target ──────────────────
FEATURES = ["Glucose", "BloodPressure", "BMI", "Age"]
TARGET = "Outcome"

X = df[FEATURES].copy()
y = df[TARGET]


# ── Step 3: Handle Invalid Medical Values ─────────────
# In PIMA dataset, 0 often means missing value

for col in ["Glucose", "BloodPressure", "BMI"]:
    X[col] = X[col].replace(0, X[col].median())

print("\nFeature Statistics After Cleaning:")
print(X.describe())


# ── Step 4: Train/Test Split ──────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"\nTraining Samples: {len(X_train)}")
print(f"Testing Samples : {len(X_test)}")


# ── Step 5: Scale Features ────────────────────────────
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# ── Step 6: Train Model ───────────────────────────────
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=6,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)


# ── Step 7: Evaluate Model ────────────────────────────
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ── Step 8: Feature Importance ────────────────────────
importances = dict(
    zip(FEATURES, model.feature_importances_)
)

print("\nFeature Importances:")
for feature, importance in sorted(
    importances.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{feature}: {importance:.3f}")


# ── Step 9: Save Model & Scaler ───────────────────────
MODEL_DIR = "notebooks/ml_models"

os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(
    model,
    f"{MODEL_DIR}/risk_model.joblib"
)

joblib.dump(
    scaler,
    f"{MODEL_DIR}/scaler.joblib"
)

print("\n✅ Model saved successfully")
print("✅ Scaler saved successfully")


# ── Step 10: Test Sample Prediction ───────────────────
sample = np.array([
    [120, 70, 25.0, 25]
])  # Glucose, BP, BMI, Age

sample_scaled = scaler.transform(sample)

risk_probability = model.predict_proba(sample_scaled)[0][1]

if risk_probability > 0.6:
    risk_level = "HIGH"
elif risk_probability > 0.3:
    risk_level = "MEDIUM"
else:
    risk_level = "LOW"

print("\nSample Prediction")
print("------------------")
print("Input:")
print("Glucose = 120")
print("Blood Pressure = 70")
print("BMI = 25.0")
print("Age = 25")

print(f"\nRisk Score : {risk_probability:.3f}")
print(f"Risk Level : {risk_level}")