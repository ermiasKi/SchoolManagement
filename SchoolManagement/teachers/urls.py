from django.urls import path, include
from rest_framework import routers
from .views import TeacherViewSet

router = routers.DefaultRouter()
router.register('teachers', TeacherViewSet, basename='teacher')

urlpatterns = [
    path('', include(router.urls)),
]