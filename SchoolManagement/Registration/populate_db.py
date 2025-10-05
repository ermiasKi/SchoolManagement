from .models import User, Student, Teacher, Admin, Subject, Score
import random
from datetime import date, timedelta
import uuid

# ----- CREATE SUBJECTS -----
subjects = ['Math', 'Physics', 'Biology', 'Chemistry', 'History', 'English', 'Computer Science']
subject_objs = [Subject.objects.create(name=s) for s in subjects]

# ----- CREATE USERS -----
def create_user(first, last, role):
    return User.objects.create(
        first_name=first,
        last_name=last,
        email=f"{first.lower()}.{last.lower()}@school.com",
        password_hash="hashedpassword123",
        role=role
    )

# Admins
admin1 = create_user("Alice", "Admin", "admin")
admin2 = create_user("Bob", "Admin", "admin")

# Teachers
teachers = []
for t in ["John Smith", "Mary Johnson", "David Brown", "Sarah Miller"]:
    first, last = t.split()
    user = create_user(first, last, "teacher")
    teachers.append(Teacher.objects.create(user=user, subject=random.choice(subjects)))

# Students
students = []
for i in range(1, 11):
    first = f"Student{i}"
    last = "Test"
    user = create_user(first, last, "student")
    students.append(Student.objects.create(
        user=user,
        grade_level=random.randint(9, 12),
        class_section=random.choice(['A', 'B', 'C'])
    ))

# Admin profiles
for u in [admin1, admin2]:
    Admin.objects.create(user=u)

# Scores
for s in students:
    for subj in subject_objs:
        Score.objects.create(
            student=s,
            teacher=random.choice(teachers),
            subject=subj,
            score=random.uniform(50, 100),
            date_assigned=date.today() - timedelta(days=random.randint(1, 100))
        )

print("✅ Mock data successfully created!")
