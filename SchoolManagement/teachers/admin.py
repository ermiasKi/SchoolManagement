from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'id', 'user', 'department')
    search_fields = ('user__username', 'department')
    filter_horizontal = ('subjects', 'assigned_classes')
