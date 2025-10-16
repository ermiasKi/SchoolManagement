from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
    

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'
    

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'
    

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, obj):
        if (request.method in SAFE_METHODS) or (getattr(obj, 'teacher', None)==request.user) or (getattr(obj, 'author', None)==request.user):
            return True
        return False

class IsOwnerOrReadOnlyS(BasePermission):
    def has_permission(self, request, obj):
        if (request.method in SAFE_METHODS) or (getattr(obj, 'teacher', None)==request.user) or (getattr(obj, 'author', None)==request.user):
            return True
        return False