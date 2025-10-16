from rest_framework import serializers
from .models import Student
from attendance.models import Attendance
from academics.models import Grade

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['date', 'status']

class GradeSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.name', read_only=True)
    class Meta:
        model = Grade
        fields = ['subject', 'score', 'remarks']

class StudentDetailSerializer(serializers.ModelSerializer):
    attendance = AttendanceSerializer(source='attendance_set', many=True, read_only=True)
    grades = GradeSerializer(many=True, read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    name = serializers.CharField(source='user.first_name', read_only=True)

    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'roll_number', 'attendance', 'grades']
