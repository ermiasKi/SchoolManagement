### 🏫 High School Website Backend Project
## 📘 Overview

This project is a backend system for a high school management website built using Django. It aims to handle student, teacher, subject, and class data efficiently while supporting user authentication, CRUD operations, and structured relationships among entities.

The backend is designed with scalability in mind and will later connect with a frontend interface for full school management functionality.

## ⚙️ Tech Stack

Python 3.12+

Django 5+

SQLite3 / PostgreSQL (configurable)

Django Generic Views & Forms

Bootstrap (for admin UI enhancement)

Virtual Environment (venv)

## 🧩 Current Features

Database schema for managing:

Students

Teachers

Classes

Subjects

Users (Custom User Model)

Django Admin panel for managing school data

Registration forms for all models using Django Forms

Basic data population script for seeding mock data

Generic class-based views for CRUD operations

Clean, modular Django app structure
---

## How to run the project

# 1. Clone the repository
git clone https://github.com/<your-username>/school-management-backend.git

# 2. Navigate into the project
cd SchoolManagement

# 3. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # (on Mac/Linux)
venv\Scripts\activate       # (on Windows)

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver
