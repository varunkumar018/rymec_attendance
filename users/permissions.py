from rest_framework import permissions

class IsClgAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is an admin
        return request.user.is_authenticated and request.user.role == 'admin'

class IsDeptAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is either a staff user or admin
        return request.user.is_authenticated and request.user.role in ['staff_user', 'admin']

# class IsStaffOrStu(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user is authenticated and is either a student, staff user, or admin
#         return request.user.is_authenticated and request.user.role in ['student', 'staff_user', 'admin']

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a staff user
        return request.user.is_authenticated and request.user.role == 'staff_user'
    
class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a student
        return request.user.is_authenticated and request.user.role == 'student'
