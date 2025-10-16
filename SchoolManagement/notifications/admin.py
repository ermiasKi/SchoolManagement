from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id','recipient', 'sender', 'message', 'is_read', 'timestamp')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('recipient__username', 'sender__username', 'message')
