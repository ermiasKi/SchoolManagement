from django.db import models
from students.models import Student
from teachers.models import Teacher

# Create your models here.

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent'), ('headsup', 'Headsup')],)
