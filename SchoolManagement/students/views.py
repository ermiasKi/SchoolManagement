from rest_framework import viewsets, permissions
from .models import Student
from .serializers import StudentDetailSerializer
from SchoolManagement.permissions import IsAdmin, IsTeacher, IsOwnerOrReadOnlyS

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['teacher', 'admin']:
            # Show all students
            return Student.objects.all().select_related('user', 'classroom').prefetch_related('grades', 'attendance_set')
        else:
            # Students can only see themselves
            return Student.objects.filter(user=user).select_related('user', 'classroom').prefetch_related('grades', 'attendance')

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)