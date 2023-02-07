from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    """Проверка пользователя на роль автора."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class IsAdminPermission(permissions.BasePermission):
    """Проверка пользователя на роль Администратора."""

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and user.is_admin
            or user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            user.is_authenticated and user.is_admin
            or user.is_superuser
        )


class IsModeratorPermission(permissions.BasePermission):
    """Проверка пользователя на роль Модератора."""

    def has_permission(self, request, view):
        user = request.user
<<<<<<< HEAD:api_yamdb/users/permissions.py
        return user.is_authenticated and user.is_moderator or user.is_staff

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_authenticated and user.is_moderator or user.is_staff
=======
        return (
            user.is_authenticated and user.is_moderator
            or user.is_staff
        )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            user.is_authenticated and user.is_moderator
            or user.is_staff
        )
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d:api_yamdb/api/permissions.py


class IsAdminOrReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.is_admin
        return False
