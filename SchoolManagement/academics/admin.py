from django.contrib import admin
from .models import Subject, ClassRoom, Grade

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    search_fields = ('name', 'code')

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'grade_level', 'year')
    list_filter = ('grade_level', 'year')
    search_fields = ('name',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'student__user__username', 'subject__name', 'teacher__user__username', 'score', 'updated_at')
    list_filter = ('subject', 'teacher')
    search_fields = ('student__user__username', 'subject__name')
