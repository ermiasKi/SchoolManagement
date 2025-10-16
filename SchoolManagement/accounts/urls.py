from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, Login, Register

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view(), name='user-login'),
    path('register/', Register.as_view(), name='user-register'),
]