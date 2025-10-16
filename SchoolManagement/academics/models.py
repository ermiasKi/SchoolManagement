from django.db import models
from django.db.models.signals import post_save
# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

class ClassRoom(models.Model):
    name = models.CharField(max_length=100)
    grade_level = models.IntegerField()
    year = models.CharField(max_length=10)

class Grade(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)