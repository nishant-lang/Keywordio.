from rest_framework import permissions


class Updatebookslist(permissions.BasePermission):
    """Allow user to edit their own profile"""
    
    def has_object_permission(self,request,view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
           return True
        
        return obj.user_profile.id==request.user.id