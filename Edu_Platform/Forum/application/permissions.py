from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

ViewForumThreadClaim = 'ViewForumThreadClaim'
ViewThreadReplyClaim = 'ViewThreadReplyClaim'
CreateForumThreadClaim = 'CreateForumThreadClaim'


class HasViewForumThreadClaim(permissions.BasePermission):
    message = 'Viewing Forum Thread is not allowed.'

    def has_permission(self, request, view):
        return ViewForumThreadClaim in request.user.claims


class HasViewThreadReplyClaim(permissions.BasePermission):
    message = 'Viewing Thread Reply is not allowed.'
    
    def has_permission(self, request, view):
        return ViewThreadReplyClaim in request.user.claims


class CanCreateForumThreadClaim(permissions.BasePermission):
    message = 'Creating Forum Thread are not allowed.'
    
    def has_permission(self, request, view):
        return CreateForumThreadClaim in request.user.claims
    