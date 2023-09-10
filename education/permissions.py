from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = 'Вы являетесь модератором!'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR and request.method in ['POST', 'DELETE']:
            return False
        return True


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user or request.user.is_superuser:
            return True
        return False