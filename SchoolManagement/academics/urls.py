from django.urls import path, include
from rest_framework import routers
from .views import SubjectViewset, ClassRoomViewset, GradeViewset

router = routers.DefaultRouter()
router.register('subjects', SubjectViewset, basename='subject')
router.register('classrooms', ClassRoomViewset, basename='classroom')
router.register('grades', GradeViewset, basename='grade')

urlpatterns = [
    path('', include(router.urls))
]