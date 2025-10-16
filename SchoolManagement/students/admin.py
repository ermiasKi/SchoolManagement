from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'student_id', 'user', 'roll_number', 'classroom', 'parent_contact', 'created_at')
    list_filter = ('classroom',)
    search_fields = ('user__username', 'roll_number')
