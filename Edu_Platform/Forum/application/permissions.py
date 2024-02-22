from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

ViewForumThreadClaim = 'ViewForumThreadClaim'
ViewThreadReplyClaim = 'ViewThreadReplyClaim'
CreateForumThreadClaim = 'CreateForumThreadClaim'
CreateThreadReplyClaim = 'CreateThreadReplyClaim'


class HasViewForumThreadClaim(permissions.BasePermission):
    message = 'Viewing Forum Thread is not allowed.'

    def has_permission(self, request, view):
        return hasattr(request.user, 'claims') and ViewForumThreadClaim in request.user.claims


class HasViewThreadReplyClaim(permissions.BasePermission):
    message = 'Viewing Thread Reply is not allowed.'
    
    def has_permission(self, request, view):
        return hasattr(request.user, 'claims') and ViewThreadReplyClaim in request.user.claims


class CanCreateForumThreadClaim(permissions.BasePermission):
    message = 'Creating Forum Thread are not allowed.'
    
    def has_permission(self, request, view):
        return hasattr(request.user, 'claims') and CreateForumThreadClaim in request.user.claims


class CanCreateThreadReplyClaim(permissions.BasePermission):
    message = 'Creating Thread Reply are not allowed.'
    
    def has_permission(self, request, view):
        return hasattr(request.user, 'claims') and CreateThreadReplyClaim in request.user.claims
    