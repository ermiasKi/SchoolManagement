import uuid
from django.db import models
from accounts.models import User

# Create your models here.



class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    roll_number = models.CharField(max_length=20, unique=True)
    classroom = models.ForeignKey('academics.ClassRoom', on_delete=models.SET_NULL, null=True)
    parent_contact = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    