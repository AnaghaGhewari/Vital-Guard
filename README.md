<div align="center">

# 🩺 VitalGuard

### AI-Powered Health Risk Monitoring Backend

#### Building a production-grade backend with FastAPI, PostgreSQL, JWT Authentication & Future ML Integration 🚀

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

### 🔐 Authentication

* User Registration
* User Login
* Password Hashing with bcrypt
* JWT Token Generation
* Secure Password Verification

### ❤️ Vital Monitoring

* Create Vital Records
* Retrieve Vital Records
* Pagination Support
* PostgreSQL Data Storage

### 🗄️ Database Layer

* PostgreSQL Integration
* SQLAlchemy ORM
* Database Sessions
* Relational Data Models

### 🛡️ API Reliability

* Pydantic Validation
* Global Exception Handling
* Structured Error Responses
* Swagger Documentation

---

## 🚧 Currently Working On

### JWT Authentication Flow

* ✅ Password Hashing (bcrypt)
* ✅ JWT Token Generation
* 🚧 get_current_user()
* 🚧 Route Protection
* 🚧 User-Specific Data Access

---

## 🛠️ Tech Stack

| Layer          | Technology       |
| -------------- | ---------------- |
| Language       | Python           |
| Backend        | FastAPI          |
| Database       | PostgreSQL       |
| ORM            | SQLAlchemy       |
| Authentication | JWT              |
| Security       | Passlib + bcrypt |
| Validation     | Pydantic         |
| Testing        | Swagger UI       |
| Future ML      | Scikit-Learn     |

---

## 📂 Project Structure

```text
vitalguard/
│
├── main.py
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
│   └── vitals.py
│
├── requirements.txt
├── .env
└── README.md
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

Use Swagger UI to test all APIs directly from the browser.

---

## 📈 Development Progress

```text
Backend Foundations     ██████████ 100%
FastAPI Setup           ██████████ 100%
PostgreSQL Setup        ██████████ 100%
SQLAlchemy ORM          ██████████ 100%
Authentication APIs     ██████████ 100%
Password Hashing        ██████████ 100%
JWT Generation          ██████████ 100%
Current User Logic      ███████░░░  70%
Route Protection        █████░░░░░  50%
User Scoped Data        ███░░░░░░░  30%
ML Integration          ░░░░░░░░░░   0%
Cloud Deployment        ░░░░░░░░░░   0%
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

### Week 3 — Authentication & Security 🚧

#### Day 1 ✅

* Password Hashing (bcrypt)

#### Day 2 ✅

* JWT Token Creation

#### Day 3 🚧

* Token Decoding
* get_current_user()

#### Day 4 🚧

* Protected Routes

#### Day 5 🚧

* User-Specific Data Access

---

## 🎯 Future Roadmap

* Health Risk Prediction Engine
* Machine Learning Integration
* Risk Scoring System
* Personalized Health Insights
* Docker Support
* Cloud Deployment
* CI/CD Pipeline

---

## 🌱 Key Concepts Learned

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* Password Hashing
* Dependency Injection
* Pydantic Validation
* Exception Handling
* API Design
* Backend Architecture

---

<div align="center">

### 🌸 Built by Anagha Ghewari

**Learning Backend Engineering by Building Real Systems**

🚀 FastAPI • PostgreSQL • JWT • AI/ML

</div>
