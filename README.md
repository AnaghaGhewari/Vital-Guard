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
* 🚧 Machine Learning Integration

---

## 🤖 AI / ML Integration

### Dataset

* PIMA Indians Diabetes Dataset

### Completed

* Dataset Added
* Training Pipeline Created (`train_model.py`)
* Feature Selection Strategy
* Data Cleaning Logic
* Train/Test Split Setup
* Feature Scaling Setup
* Random Forest Configuration

### In Progress

* Model Training
* Model Evaluation
* Feature Importance Analysis
* Model Serialization
* FastAPI Integration
* Risk Prediction Endpoint

---

## 🛠️ Tech Stack

| Layer            | Technology       |
| ---------------- | ---------------- |
| Language         | Python           |
| Backend          | FastAPI          |
| Database         | PostgreSQL       |
| ORM              | SQLAlchemy       |
| Authentication   | JWT              |
| Authorization    | OAuth2           |
| Security         | Passlib + bcrypt |
| Validation       | Pydantic         |
| Migrations       | Alembic          |
| Testing          | Swagger UI       |
| Machine Learning | Scikit-Learn     |

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
├── notebooks/
│   ├── datasets/
│   │   └── diabetes.csv
│   │
│   └── train_model.py
│
├── requirements.txt
├── alembic.ini
├── .env
└── README.md
```

---

## 🔗 Implemented API Routes

### Authentication

```http
POST /api/v1/auth/register
POST /api/v1/auth/login
```

### User

```http
GET  /api/v1/user/me
PUT  /api/v1/user/me
```

### Vitals

```http
POST   /api/v1/vitals
GET    /api/v1/vitals
GET    /api/v1/vitals/{id}
DELETE /api/v1/vitals/{id}
```

### Risk

```http
GET /api/v1/risk/score
```

---

## 🚀 Running The Project

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI Server

```bash
uvicorn main:app --reload
```

---

## 📘 API Documentation

After starting the server:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides interactive testing for all endpoints.

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
Training Pipeline       ██████████ 100%
Data Cleaning           ██████████ 100%
Feature Engineering     ███████░░░  70%
Model Training          ███░░░░░░░  30%
Model Evaluation        ░░░░░░░░░░   0%
FastAPI ML Integration  ░░░░░░░░░░   0%

Cloud Deployment        ░░░░░░░░░░   0%
Frontend Development    ░░░░░░░░░░   0%
```

---

## 📝 Learning Journey

### Week 1 — Backend Foundations ✅

* REST APIs
* JSON Handling
* HTTP Methods
* Decorators
* Exception Handling
* Git & GitHub

### Week 2 — FastAPI & Databases ✅

* FastAPI Architecture
* Routers
* Schemas
* PostgreSQL
* SQLAlchemy
* CRUD Operations

### Week 3 — Authentication & Security ✅

#### Day 1

* Password Hashing (bcrypt)

#### Day 2

* JWT Token Creation

#### Day 3

* Token Decoding
* get_current_user()

#### Day 4

* Protected Routes
* OAuth2 Authentication

#### Day 5

* User-Specific Data Access
* JWT Authorization Flow
* Swagger OAuth Integration

### Week 4 — Risk Analysis & Machine Learning 🚧

#### Completed

* Risk Route Implementation
* Risk Response Schemas
* PIMA Diabetes Dataset Integration
* ML Training Pipeline Setup

#### In Progress

* Model Training
* Model Evaluation
* FastAPI Model Integration
* AI-Powered Risk Prediction

---

## 🎯 Future Roadmap

### Backend

* Health Trend Analytics
* Advanced Risk Engine
* Notifications & Alerts
* Role-Based Access Control

### AI / ML

* Diabetes Risk Prediction
* Personalized Health Insights
* Explainable AI Responses
* Recommendation Engine

### DevOps & Cloud

* Docker
* CI/CD Pipeline
* AWS Deployment
* Monitoring & Logging

---

## 🌱 Key Concepts Learned

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* OAuth2
* Password Hashing
* Dependency Injection
* User Authorization
* Route Protection
* Alembic Migrations
* Pydantic Validation
* Exception Handling
* API Design
* Backend Architecture

---

<div align="center">

### 🌸 Built by Anagha Ghewari

**Learning Backend Engineering, AI/ML & Cloud Computing by Building Real Systems**

🚀 FastAPI • PostgreSQL • JWT • OAuth2 • Scikit-Learn

</div>
