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
        return user.is_authenticated and user.is_admin or user.is_superuser

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_authenticated and user.is_admin or user.is_superuser


class IsModeratorPermission(permissions.BasePermission):
    """Проверка пользователя на роль Модератора."""

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_moderator or user.is_staff

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_authenticated and user.is_moderator or user.is_staff
