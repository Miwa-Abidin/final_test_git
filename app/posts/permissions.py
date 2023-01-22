from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS or
            (
                request.user and
                request.user.is_authenticated and
                obj.author == request.user.author
            )
        )