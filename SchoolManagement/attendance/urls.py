from django.urls import path, include
from rest_framework import routers
from .views import AttendanceViewset

router = routers.DefaultRouter()
router.register('attendaces', AttendanceViewset, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
]