from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'sender', 'target_role', 'created_at')
    list_filter = ('target_role',)
    search_fields = ('title', 'content', 'sender__username')
