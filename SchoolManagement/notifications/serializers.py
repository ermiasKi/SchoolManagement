from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    recipient = serializers.CharField(source='recipient.username', read_only=True)
    sender = serializers.CharField(source='sender.username', read_only=True)
    class Meta:
        model = Notification
        fields = ['recipient', 'sender', 'message', 'is_read']