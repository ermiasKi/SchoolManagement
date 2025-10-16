from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'teacher', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('student__user__username', 'teacher__user__username')
