from rest_framework import permissions
from rest_framework.permissions import BasePermission



class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # if request.method == 'GET':
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class ViewPatientHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('profile.view_history')