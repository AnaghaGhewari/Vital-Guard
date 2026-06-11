<div align="center">

# 🩺 VitalGuard

### AI-Powered Health Risk Monitoring Backend

#### Building a production-grade backend with FastAPI, PostgreSQL, JWT Authentication, OAuth2 & AI-Driven Risk Analysis 🚀

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success?style=for-the-badge\&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge\&logo=postgresql)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=for-the-badge)

</div>

---

## 🌟 Overview

VitalGuard is an AI-powered health monitoring platform designed to securely collect health vitals, manage user data, and serve as the foundation for future machine learning-based health risk prediction.

This project is being built as part of my Backend Engineering, AI/ML, and Cloud Computing learning journey.

---

## ✨ Features Implemented

### 🔐 Authentication & Security

* User Registration
* User Login
* Password Hashing with bcrypt
* JWT Token Generation
* JWT Token Validation
* OAuth2 Authentication Flow
* Protected Routes
* Current User Authentication
* User-Specific Access Control

### ❤️ Vital Monitoring

* Create Vital Records
* Retrieve Vital Records
* Pagination Support
* User-Scoped Health Data
* PostgreSQL Data Storage

### 👤 User Management

* Get Current User Profile
* Update Current User Profile
* Active User Validation

### 📊 Risk Analysis

* Risk Score Endpoint
* Health Risk Evaluation
* Risk Response Generation
* Foundation for Future ML Predictions

### 🗄️ Database Layer

* PostgreSQL Integration
* SQLAlchemy ORM
* Database Sessions
* Relational Data Models
* Alembic Migration Setup

### 🛡️ API Reliability

* Pydantic Validation
* Global Exception Handling
* Structured Error Responses
* Swagger Documentation
* OAuth2 Authorization Support

---

## 🚀 Current Milestones

* ✅ FastAPI Backend Architecture
* ✅ PostgreSQL Integration
* ✅ SQLAlchemy ORM
* ✅ JWT Authentication
* ✅ OAuth2 Authorization
* ✅ Protected Routes
* ✅ User-Scoped Data Isolation
* ✅ Risk Analysis API
* ✅ Alembic Migration Setup
* ✅ Machine Learning Model Training
* ✅ Model Serialization
* ✅ ML-Powered Risk Prediction API

---

## 🤖 AI / ML Integration

### Dataset

* PIMA Indians Diabetes Dataset

### Completed

* Dataset Added
* Data Cleaning Pipeline
* Feature Selection
* Train/Test Split
* Feature Scaling using StandardScaler
* Random Forest Model Training
* Model Evaluation
* Feature Importance Analysis
* Model Serialization with Joblib
* Risk Engine Service Layer
* FastAPI Model Integration
* Real-Time Risk Prediction Endpoint

### Model Features

The model currently uses:

* Glucose
* Blood Pressure
* BMI
* Age

to predict diabetes risk probability.

### Prediction Workflow

```text
User Health Data
        ↓
Data Validation
        ↓
Feature Scaling
        ↓
Random Forest Model
        ↓
Risk Probability
        ↓
Risk Classification
        ↓
API Response
```

---

## 📂 Project Structure

```text
vitalguard/
│
├── main.py
│
├── alembic/
│   ├── env.py
│   └── versions/
│
├── core/
│   ├── config.py
│   ├── security.py
│   ├── dependencies.py
│   └── exception.py
│
├── db/
│   └── session.py
│
├── models/
│   ├── user.py
│   └── vital.py
│
├── schemas/
│   ├── user.py
│   └── vital.py
│
├── routers/
│   ├── auth.py
│   ├── users.py
│   ├── vitals.py
│   └── risk.py
│
├── services/
│   └── risk_engine.py
│
├── notebooks/
│   ├── dataset/
│   │   └── diabetes.csv
│   │
│   ├── ml_models/
│   │   ├── risk_model.joblib
│   │   └── scaler.joblib
│   │
│   └── train_model.py
│
├── requirements.txt
├── alembic.ini
├── .env
└── README.md
```

---

## 📈 Development Progress

```text
Backend Foundations     ██████████ 100%
FastAPI Setup           ██████████ 100%
PostgreSQL Setup        ██████████ 100%
SQLAlchemy ORM          ██████████ 100%
Authentication APIs     ██████████ 100%
Password Hashing        ██████████ 100%
JWT Authentication      ██████████ 100%
OAuth2 Integration      ██████████ 100%
Current User Logic      ██████████ 100%
Route Protection        ██████████ 100%
User Scoped Data        ██████████ 100%
Risk Analysis API       ██████████ 100%
Alembic Setup           ██████████ 100%

ML Dataset Setup        ██████████ 100%
Data Cleaning           ██████████ 100%
Feature Engineering     ██████████ 100%
Model Training          ██████████ 100%
Model Evaluation        ██████████ 100%
Model Serialization     ██████████ 100%
Risk Engine Service     ██████████ 100%
FastAPI ML Integration  ██████████ 100%

Cloud Deployment        ░░░░░░░░░░   0%
Frontend Development    ░░░░░░░░░░   0%
```

---

### Week 4 — Risk Analysis & Machine Learning ✅

#### Completed

* Risk Route Implementation
* Risk Response Schemas
* PIMA Diabetes Dataset Integration
* Data Cleaning Pipeline
* Random Forest Model Training
* Feature Scaling
* Model Evaluation
* Model Serialization using Joblib
* Risk Engine Service Layer
* FastAPI Model Integration
* Real-Time Risk Prediction API

#### Next

* Personalized Health Recommendations
* Explainable AI Responses
* Prediction History Tracking
* Cloud Deployment

```

### 🌸 Built by Anagha Ghewari

**Learning Backend Engineering, AI/ML & Cloud Computing by Building Real Systems**

🚀 FastAPI • PostgreSQL • JWT • OAuth2 • Scikit-Learn • Random Forest
```
