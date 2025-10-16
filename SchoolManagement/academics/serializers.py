from students.models import Student
from teachers.models import Teacher
from rest_framework import serializers
from .models import Subject, ClassRoom, Grade



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'code']


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"

class GradeSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.username', read_only=True)
    teacher = serializers.CharField(source='teacher.user.username', read_only=True)
    subject = serializers.CharField(source='subject.name', read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), 
        source='student'  # This maps student_id to student field
    )
    subject_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), 
        source='subject'
    )
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        source='teacher'
    )
    class Meta:
        model = Grade
        fields = ['student_id', 'subject_id', 'teacher_id', 'student', 'subject', 'teacher', 'score', 'remarks']




class StudentSummarySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Student
        fields = ['student_id', 'user', 'roll_number']

class TeacherSummarySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Teacher
        fields = ['user', 'department']

class ClassRoomDetailSerializer(serializers.ModelSerializer):
    students = StudentSummarySerializer(source='student_set', many=True, read_only=True)
    teachers = TeacherSummarySerializer(many=True, read_only=True)

    class Meta:
        model = ClassRoom
        fields = ['id', 'name', 'grade_level', 'year', 'students', 'teachers']
