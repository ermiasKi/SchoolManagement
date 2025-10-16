from django.shortcuts import render
from rest_framework import viewsets
from .models import Announcement
from .serializers import AnnouncementSerializer
from SchoolManagement.permissions import IsAdmin, IsTeacher, IsOwnerOrReadOnly

# Create your views here.

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all().order_by('-created_at')
    serializer_class = AnnouncementSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [IsAdmin() or IsTeacher()]
        return [IsOwnerOrReadOnly()]
    
    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)