<div align="center">

# 🩺 VitalGuard

### AI-Powered Health Risk Monitoring Platform

#### Building a production-style backend using FastAPI, PostgreSQL, JWT & Machine Learning 🚀

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success?style=for-the-badge\&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge\&logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange?style=for-the-badge)

<br>

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=flat-square)
![Version](https://img.shields.io/badge/Version-v0.3-blue?style=flat-square)

</div>

---

> 🚧 This project is actively being developed as part of my Backend Engineering, AI/ML, and Cloud Computing learning journey.

---

## 🌟 About VitalGuard

VitalGuard is an AI-powered health monitoring backend designed to collect user vitals, manage health records securely, and serve as the foundation for future machine learning-driven health risk prediction.

The project focuses on learning real-world backend development practices while building a scalable healthcare platform from scratch.

---

## ✨ Current Features

### 🔐 Authentication

* User Registration
* User Login
* Password Hashing with bcrypt
* JWT Token Generation
* Secure Authentication Flow

### ❤️ Vital Monitoring

* Log Daily Health Vitals
* Retrieve Vital Records
* Pagination Support
* Persistent Database Storage

### 🗄️ Database

* PostgreSQL Integration
* SQLAlchemy ORM
* Relational Data Modeling
* Session Management

### 📄 Developer Experience

* Swagger UI Documentation
* Pydantic Validation
* Structured API Responses
* Global Exception Handling

---

## 🛠️ Tech Stack

| Category       | Technology       |
| -------------- | ---------------- |
| Language       | Python           |
| Framework      | FastAPI          |
| Database       | PostgreSQL       |
| ORM            | SQLAlchemy       |
| Authentication | JWT              |
| Security       | Passlib + bcrypt |
| Validation     | Pydantic         |
| API Testing    | Swagger UI       |
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
│   └── exception.py
│
├── db/
│   └── session.py
│
├── routers/
│   ├── auth.py
│   ├── users.py
│   └── vitals.py
│
├── schemas/
│   ├── user.py
│   └── vital.py
│
├── models/
│   ├── user.py
│   └── vital.py
│
├── .env
├── requirements.txt
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

### Run The Server

```bash
uvicorn main:app --reload
```

---

## 📘 API Documentation

Once the server is running:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides interactive testing for every endpoint.

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
Current User Logic      ██████░░░░  60%
Protected Routes        ░░░░░░░░░░   0%
User Scoped Data        ░░░░░░░░░░   0%
ML Integration          ░░░░░░░░░░   0%
Cloud Deployment        ░░░░░░░░░░   0%
```

---

## 📝 Learning Journey

### Week 1 — Backend Foundations ✅

* HTTP & REST APIs
* JSON Handling
* Decorators
* Exception Handling
* Mock Servers
* Git & GitHub Workflow

### Week 2 — FastAPI & Databases ✅

* FastAPI Setup
* Project Architecture
* API Routers
* Pydantic Schemas
* PostgreSQL
* SQLAlchemy ORM
* CRUD Operations

### Week 3 — Authentication & Security 🚧

#### Day 1 ✅

* Password Hashing (bcrypt)

#### Day 2 ✅

* JWT Token Creation
* Authentication Flow

#### Day 3 🚧

* Token Decoding
* get_current_user()

#### Day 4 ⏳

* Protected Routes

#### Day 5 ⏳

* User-Scoped Data

---

## 🎯 Current Status

### Completed

* ✅ User Registration
* ✅ User Login
* ✅ Password Hashing
* ✅ JWT Token Generation
* ✅ PostgreSQL Integration
* ✅ SQLAlchemy ORM
* ✅ Vital Tracking APIs
* ✅ Swagger Documentation
* ✅ Global Exception Handling

### In Progress

* 🚧 User Authentication Middleware
* 🚧 Current User Resolution
* 🚧 Authorization Flow

### Planned

* ⏳ Health Risk Scoring
* ⏳ Machine Learning Models
* ⏳ Personalized Health Insights
* ⏳ Docker Deployment
* ⏳ Cloud Hosting

---

## 🌱 Key Concepts Learned

* FastAPI
* REST APIs
* PostgreSQL
* SQLAlchemy ORM
* JWT Authentication
* Password Hashing
* Dependency Injection
* Pydantic Validation
* Exception Handling
* Backend Project Architecture

---

<div align="center">

### 🌸 Built by Anagha Ghewari

*"Learning backend engineering by building real-world systems one commit at a time."*

🚀 FastAPI • PostgreSQL • JWT • AI/ML

</div>
