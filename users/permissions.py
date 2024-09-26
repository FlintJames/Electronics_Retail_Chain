from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsActive(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_active:
            return True
        return False
