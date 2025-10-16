import uuid
from django.db import models
from accounts.models import User
from academics.models import Subject, ClassRoom

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    department = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    assigned_classes = models.ManyToManyField(ClassRoom, related_name='teachers')