from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(read_only=True, source='teacher.user.username')
    student = serializers.CharField(read_only=True, source='student.user.username')
    class Meta:
        model = Attendance
        fields = ['student', 'teacher', 'status']
    