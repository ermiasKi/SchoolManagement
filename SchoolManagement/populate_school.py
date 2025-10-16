from django.utils import timezone
from accounts.models import User
from academics.models import Subject, ClassRoom, Grade
from teachers.models import Teacher
from students.models import Student
from attendance.models import Attendance
from announcements.models import Announcement
from notifications.models import Notification

# 🧹 Clear all existing data
print("Cleaning up old data...")
Notification.objects.all().delete()
Attendance.objects.all().delete()
Grade.objects.all().delete()
Teacher.objects.all().delete()
Student.objects.all().delete()
ClassRoom.objects.all().delete()
Subject.objects.all().delete()
Announcement.objects.all().delete()
User.objects.all().delete()
print("✅ Database cleared.")

# 👥 Create Users
print("Creating users...")
admin = User.objects.create(
    username="admin_user",
    first_name="Admin",
    last_name="User",
    email="admin@school.com",
    password_hash="hashed_admin_pass",
    role="admin"
)

t1_user = User.objects.create(username="anna_smith", first_name="Anna", last_name="Smith", email="anna@school.com", password_hash="pass123", role="teacher")
t2_user = User.objects.create(username="ben_johnson", first_name="Ben", last_name="Johnson", email="ben@school.com", password_hash="pass123", role="teacher")

s1_user = User.objects.create(username="john_doe", first_name="John", last_name="Doe", email="john@student.com", password_hash="pass123", role="student")
s2_user = User.objects.create(username="emma_stone", first_name="Emma", last_name="Stone", email="emma@student.com", password_hash="pass123", role="student")
s3_user = User.objects.create(username="mike_lee", first_name="Mike", last_name="Lee", email="mike@student.com", password_hash="pass123", role="student")
s4_user = User.objects.create(username="sara_kim", first_name="Sara", last_name="Kim", email="sara@student.com", password_hash="pass123", role="student")
s5_user = User.objects.create(username="lily_adams", first_name="Lily", last_name="Adams", email="lily@student.com", password_hash="pass123", role="student")

# 📚 Subjects
print("Creating subjects...")
math = Subject.objects.create(name="Mathematics", code="MATH101")
physics = Subject.objects.create(name="Physics", code="PHYS101")
chemistry = Subject.objects.create(name="Chemistry", code="CHEM101")
biology = Subject.objects.create(name="Biology", code="BIO101")
english = Subject.objects.create(name="English", code="ENG101")

# 🏫 Classrooms
print("Creating classrooms...")
class10A = ClassRoom.objects.create(name="10A", grade_level=10, year="2025")
class10B = ClassRoom.objects.create(name="10B", grade_level=10, year="2025")

# 👩‍🏫 Teachers
print("Creating teachers...")
teacher1 = Teacher.objects.create(user=t1_user, department="Science")
teacher2 = Teacher.objects.create(user=t2_user, department="Mathematics")

teacher1.subjects.add(physics, chemistry)
teacher1.assigned_classes.add(class10A)
teacher2.subjects.add(math, english)
teacher2.assigned_classes.add(class10B)

# 🎓 Students
print("Creating students...")
s1 = Student.objects.create(user=s1_user, roll_number="S1001", classroom=class10A, parent_contact="0911223344")
s2 = Student.objects.create(user=s2_user, roll_number="S1002", classroom=class10A, parent_contact="0911334455")
s3 = Student.objects.create(user=s3_user, roll_number="S1003", classroom=class10B, parent_contact="0911445566")
s4 = Student.objects.create(user=s4_user, roll_number="S1004", classroom=class10B, parent_contact="0911556677")
s5 = Student.objects.create(user=s5_user, roll_number="S1005", classroom=class10B, parent_contact="0911667788")

# 🧾 Grades
print("Assigning grades...")
Grade.objects.create(student=s1, subject=math, teacher=teacher2, score=92.5, remarks="Excellent work!")
Grade.objects.create(student=s2, subject=math, teacher=teacher2, score=85.0, remarks="Good progress")
Grade.objects.create(student=s3, subject=physics, teacher=teacher1, score=78.0, remarks="Needs improvement in lab work")
Grade.objects.create(student=s4, subject=chemistry, teacher=teacher1, score=89.5, remarks="Strong performance")
Grade.objects.create(student=s5, subject=english, teacher=teacher2, score=94.0, remarks="Excellent writing skills")

# 🗓 Attendance
print("Recording attendance...")
Attendance.objects.create(student=s1, teacher=teacher2, status="present")
Attendance.objects.create(student=s2, teacher=teacher2, status="absent")
Attendance.objects.create(student=s3, teacher=teacher1, status="headsup")
Attendance.objects.create(student=s4, teacher=teacher1, status="present")
Attendance.objects.create(student=s5, teacher=teacher2, status="present")

# 📣 Announcements
print("Creating announcements...")
Announcement.objects.create(sender=admin, title="School Reopening", content="School reopens on Monday. Be prepared!", target_role="all")
Announcement.objects.create(sender=t1_user, title="Physics Assignment", content="Submit lab report by Friday.", target_role="student")

# 🔔 Notifications
print("Creating notifications...")
Notification.objects.create(recipient=s1_user, sender=t1_user, message="New assignment posted for Physics.")
Notification.objects.create(recipient=s2_user, sender=t2_user, message="You have been marked absent today.")
Notification.objects.create(recipient=t1_user, sender=admin, message="Staff meeting scheduled for Wednesday.")
Notification.objects.create(recipient=t2_user, sender=admin, message="Submit midterm grades by next week.")

print("✅ School Management system populated successfully!")
