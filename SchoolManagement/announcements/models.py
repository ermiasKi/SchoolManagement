from django.db import models
from accounts.models import User

# Create your models here.

class Announcement(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    target_role = models.CharField(max_length=10, choices=[('student', 'Student'), ('teacher', 'Teacher'), ('all', 'All')])
    created_at = models.DateTimeField(auto_now_add=True)
