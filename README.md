<div align="center">

# 🩺 VitalGuard

### AI-Powered Health Risk Monitoring Backend

#### Building a Production-Grade Backend with FastAPI, PostgreSQL, JWT Authentication, OAuth2 & Machine Learning 🚀

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success?style=for-the-badge\&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge\&logo=postgresql)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML_Model-yellow?style=for-the-badge\&logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=for-the-badge)

</div>

---

## 🌟 Overview

VitalGuard is an AI-powered health monitoring platform designed to securely collect health data, manage user accounts, and provide personalized chronic disease risk predictions using Machine Learning.

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

### ❤️ Health Monitoring

* Create Vital Records
* Retrieve Vital Records
* Pagination Support
* User-Scoped Health Data
* PostgreSQL Data Storage

### 🤖 Machine Learning

* PIMA Indians Diabetes Dataset
* Data Cleaning Pipeline
* Feature Engineering
* StandardScaler Integration
* Random Forest Classifier
* Model Evaluation
* Feature Importance Analysis
* Model Serialization using Joblib
* ML Risk Prediction Service
* Real-Time Prediction API

### 📊 Risk Analysis

* Risk Score Endpoint
* Personalized Risk Assessment
* Risk Level Classification
* Explanation Generation
* Risk History Foundation

### 🗄️ Database Layer

* PostgreSQL Integration
* SQLAlchemy ORM
* Database Sessions
* Relational Data Models
* Alembic Migration Support

### 🛡️ API Reliability

* Pydantic Validation
* Global Exception Handling
* Structured Error Responses
* Swagger Documentation
* OAuth2 Authorization Support

---

## 🤖 Machine Learning Pipeline

### Dataset

PIMA Indians Diabetes Dataset

### Features Used

* Glucose
* Blood Pressure
* BMI
* Age

### ML Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Feature Scaling
   ↓
Random Forest Training
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
Risk Engine Service
   ↓
FastAPI Integration
   ↓
Prediction API
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
│   ├── vital.py
│   └── risk.py
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
JWT Authentication      ██████████ 100%
OAuth2 Integration      ██████████ 100%
Route Protection        ██████████ 100%
User Scoped Data        ██████████ 100%
Risk Analysis API       ██████████ 100%
Alembic Setup           ██████████ 100%

Dataset Integration     ██████████ 100%
Data Cleaning           ██████████ 100%
Feature Engineering     ██████████ 100%
Model Training          ██████████ 100%
Model Evaluation        ██████████ 100%
Model Serialization     ██████████ 100%
Risk Engine Service     ██████████ 100%
ML API Integration      ██████████ 100%

Prediction History      ███░░░░░░░  30%
SHAP Explainability     ███░░░░░░░  30%
Cloud Deployment        ░░░░░░░░░░   0%
Frontend Development    ░░░░░░░░░░   0%
```

---

## 🎯 Current API Endpoints

### Authentication

* POST `/api/v1/auth/register`
* POST `/api/v1/auth/login`

### Users

* GET `/api/v1/user/me`
* PUT `/api/v1/user/me`

### Vitals

* POST `/api/v1/vitals`
* GET `/api/v1/vitals`
* GET `/api/v1/vitals/{id}`
* DELETE `/api/v1/vitals/{id}`

### Risk Analysis

* GET `/api/v1/risk/score`
* GET `/api/v1/risk/history`

---

## 🎯 Future Roadmap

* SHAP Explainability
* Personalized Health Recommendations
* Risk Trend Analytics
* Docker Containerization
* CI/CD Pipeline
* Cloud Deployment
* React Frontend
* Real-Time Health Monitoring

---

## 🌱 Key Concepts Learned

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* OAuth2
* Alembic
* Dependency Injection
* API Design
* Machine Learning Pipelines
* Feature Engineering
* Random Forest Models
* Model Serialization
* ML Deployment
* Backend Architecture

---

<div align="center">

### 🌸 Built by Anagha Ghewari

**Learning Backend Engineering, AI/ML & Cloud Computing by Building Real Systems**

🚀 FastAPI • PostgreSQL • JWT • OAuth2 • Scikit-Learn • Random Forest

</div>
