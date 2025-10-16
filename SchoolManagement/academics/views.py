from django.shortcuts import render
from rest_framework import permissions, viewsets
from SchoolManagement.permissions import IsAdmin, IsOwnerOrReadOnly, IsTeacher, IsStudent
from .models import ClassRoom, Grade, Subject
from .serializers import ClassRoomSerializer, GradeSerializer, SubjectSerializer, ClassRoomDetailSerializer

# Create your views here.

class SubjectViewset(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdmin]


class ClassRoomViewset(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all().prefetch_related('teachers', 'student_set')
    serializer_class = ClassRoomDetailSerializer
    permission_classes = [IsAdmin]


class GradeViewset(viewsets.ModelViewSet):
    queryset = Grade.objects.all().select_related('student', 'teacher', 'subject')
    serializer_class = GradeSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'list']:
            return [IsTeacher()]
        return [IsOwnerOrReadOnly()]