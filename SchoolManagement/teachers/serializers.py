from rest_framework import serializers
from .models import Teacher
from academics.serializers import SubjectSerializer, ClassRoomSerializer



class TeacherSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    assigned_classes = ClassRoomSerializer(many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = ['user', 'subjects', 'department', 'assigned_classes']