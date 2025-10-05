from django import forms
from .models import User, Student, Teacher, Admin, Subject, Score

# ---- USER FORM ----
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'role']


# ---- STUDENT FORM ----
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'grade_level', 'class_section']


# ---- TEACHER FORM ----
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'subject']


# ---- ADMIN FORM ----
class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['user']


# ---- SUBJECT FORM ----
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']


# ---- SCORE FORM ----
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['student', 'teacher', 'subject', 'score', 'date_assigned']
