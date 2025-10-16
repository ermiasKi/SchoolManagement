from django.shortcuts import render
from rest_framework import viewsets
from .models import Attendance
from teachers.models import Teacher
from .serializers import AttendanceSerializer
from SchoolManagement.permissions import IsAdmin, IsTeacher, IsOwnerOrReadOnly

# Create your views here.

class AttendanceViewset(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().select_related('student', 'teacher')
    serializer_class = AttendanceSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'list']:
            return [IsTeacher()]
        return [IsOwnerOrReadOnly()]
    
    def perform_create(self, serializer):
        teacher = Teacher.objects.get(user=self.request.user)
        return serializer.save(teacher=teacher)