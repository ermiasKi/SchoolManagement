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

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ermiasKi/SchoolManagement.git
cd SchoolManagement
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3️⃣ Install Dependencies

```bash
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
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server

```bash
python manage.py runserver
```

---

## 🔗 API Endpoints Overview

### 🧍‍♂️ Authentication

| Method | Endpoint              | Description         |
| ------ | --------------------- | ------------------- |
| POST   | `/accounts/register/` | Register new user   |
| POST   | `/accounts/login/`    | Login and get token |
| GET    | `/accounts/users/`    | View all users      |

### 🎓 Academics

| Method   | Endpoint                 | Description           |
| -------- | ------------------------ | --------------------- |
| GET/POST | `/academics/subjects/`   | Manage subjects       |
| GET/POST | `/academics/classrooms/` | Manage classrooms     |
| GET/POST | `/academics/grades/`     | Record or view grades |

### 🧑‍🏫 Teachers & Students

| Method   | Endpoint                   | Description                                    |
| -------- | -------------------------- | ---------------------------------------------- |
| GET/POST | `/teachers/teachers/`      | Manage teachers                                |
| GET/POST | `/students/students/`      | Manage students                                |
| GET      | `/students/students/{id}/` | View student details (attendance, score, etc.) |

### 📅 Attendance

| Method   | Endpoint                  | Description             |
| -------- | ------------------------- | ----------------------- |
| GET/POST | `/attendance/attendaces/` | Mark or view attendance |

### 📣 Announcements

| Method   | Endpoint                        | Description          |
| -------- | ------------------------------- | -------------------- |
| GET/POST | `/announcements/announcements/` | Manage announcements |

### 🔔 Notifications

| Method | Endpoint                        | Description             |
| ------ | ------------------------------- | ----------------------- |
| GET    | `/notifications/notifications/` | View user notifications |

---

## 🧩 Notifications Logic

* **Signals** trigger notifications automatically when:

  * A teacher updates attendance or grades.
  * A teacher/admin creates an announcement.
* Notifications include:

  * Sender (creator of the action)
  * Receiver (target user)
  * Message content
  * Timestamp
  * Read/unread status

---

## 📊 Example Workflow

1. **Admin** registers users (students, teachers).
2. **Teacher** records attendance and grades → student receives notification.
3. **Admin/Teacher** creates announcement → targeted notifications sent automatically.
4. **Students** log in to view grades, attendance, and unread notifications.

---

## 🧪 Testing APIs

Use **Postman** or `curl` to test the following workflow:

1. Register and login a user → get token
2. Create subjects and classrooms
3. Register students and assign classrooms
4. Create teacher and assign subjects/classes
5. Record attendance and grades → check notifications
6. Create announcement → check targeted delivery
7. Retrieve all notifications for the logged-in user

---

## 👥 Contributors

**Developer:** Ermias Kindalem
**Framework:** Django REST Framework
**Version:** 1.0.0

---
