# 🏫 School Management System (Django + DRF)

A complete **School Management System API** built using **Django** and **Django REST Framework (DRF)**.
This system manages students, teachers, classes, grades, attendance, announcements, and notifications — providing an efficient backend for digital school administration.

---

## 🚀 Features

### 👨‍🏫 User Management

* Custom `User` model with role-based access (`Admin`, `Teacher`, `Student`).
* Token-based authentication system using Django REST Framework’s `authtoken`.
* Secure registration and login endpoints.

### 📚 Academic Management

* Manage **Subjects**, **Classrooms**, and **Grades**.
* Automatically track which **Teacher** teaches which **Subject** or **Classroom**.
* Students can view their grades and classroom assignments.

### 🧑‍🎓 Student & Teacher Profiles

* Students and teachers have one-to-one linked user accounts.
* Teachers can record grades, attendance, and view classroom rosters.
* Admins can view and manage all user data centrally.

### 🗓 Attendance System

* Teachers can mark attendance (`present`, `absent`, or `headsup`).
* Notifications automatically sent to students when attendance or scores are updated.

### 📢 Announcements

* Admins and teachers can post announcements.
* Targeted delivery based on role (`student`, `teacher`, or `all`).

### 🔔 Notifications

* Automatic notifications for:

  * Grade updates
  * Attendance changes
  * New announcements
* Real-time alerts via signal-based architecture.

---

## 🧩 System Architecture

The project is divided into modular Django apps:

| App               | Purpose                                              |
| ----------------- | ---------------------------------------------------- |
| **accounts**      | Custom user model, authentication, and authorization |
| **students**      | Student profile management                           |
| **teachers**      | Teacher profile management                           |
| **academics**     | Classrooms, subjects, and grades                     |
| **attendance**    | Attendance tracking                                  |
| **announcements** | School-wide announcements                            |
| **notifications** | Automated event-based notifications                  |

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Authentication:** DRF Token Authentication
* **Storage:** Local (for profile pictures)
* **API Testing:** Postman
* **Language:** Python 3.12

---

## 🧠 Key Concepts Implemented

* Role-based permissions and access control
* Automatic notifications using Django signals
* Efficient data querying with `select_related()` and `prefetch_related()`
* Filtering, searching, and pagination for large datasets
* RESTful API design using DRF `ViewSets` and routers

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
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY='your-secret-key'
NAME='school_management_db'
USER='postgres'
PASSWORD='your-db-password'
HOST='localhost'
PORT='5432'
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver
