from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer
from SchoolManagement.permissions import IsAdmin, IsOwnerOrReadOnly, IsTeacher

# Create your views here.

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_permissions(self):
        if self.action in ['list', 'destroy']:
            return [IsAdmin()]
        if self.action in ['create']:
            return [IsTeacher()]
        return [IsOwnerOrReadOnly()]
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)