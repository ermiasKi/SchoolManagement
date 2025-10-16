from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.permissions import IsAuthenticated

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only notifications that belong to the logged-in user
        return Notification.objects.filter(recipient=self.request.user).select_related('sender', 'recipient')

    @action(detail=False, methods=['post'])
    def mark_read(self, request):
        Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
        return Response({"message": "Notifications marked as read"}, status=status.HTTP_200_OK)
