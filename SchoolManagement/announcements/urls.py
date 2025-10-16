from django.urls import path, include
from rest_framework import routers
from .views import AnnouncementViewSet

router = routers.DefaultRouter()
router.register('announcements', AnnouncementViewSet, basename='announcement')

urlpatterns = [
    path('', include(router.urls)),
]