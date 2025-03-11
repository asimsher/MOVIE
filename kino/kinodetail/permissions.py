from rest_framework import permissions

# class CheckPermissions( permissions.BasePermission ):
#     def has_permission(self, request, view):
#         if request.user == view.basename:
#             return True
#         return False


class MethodCheck( permissions.BasePermission ):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == view.basename
