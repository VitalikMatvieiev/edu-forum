from rest_framework import permissions

ViewForumThreadClaim = 'ViewForumThreadClaim'
ViewThreadReplyClaim = 'ViewThreadReplyClaim'
CreateForumThreadClaim = 'CreateForumThreadClaim'
CreateThreadReplyClaim = 'CreateThreadReplyClaim'
UpdateForumThreadClaim = 'UpdateForumThreadClaim'
UpdateThreadReplyClaim = 'UpdateThreadReplyClaim'
DeleteForumThreadClaim = 'DeleteForumThreadClaim'
DeleteThreadReplyClaim = 'DeleteThreadReplyClaim'


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


class CanUpdateForumThreadClaim(permissions.BasePermission):
    message = 'Update Forum Thread are not allowed.'
    
    def has_permission(self, request, view):
        # Check if the user has the claim at a general level
        return hasattr(request.user, 'claims') and UpdateForumThreadClaim in request.user.claims
    

class CanUpdateThreadReplyClaim(permissions.BasePermission):
    message = 'Update Thread Reply are not allowed.'
    
    def has_permission(self, request, view):
        return hasattr(request.user, 'claims') and UpdateThreadReplyClaim in request.user.claims


class CanDeleteForumThreadClaim(permissions.BasePermission):
    message = 'Delete Forum Thread are not allowed.'
    
    def has_permission(self, request, view):
        return hasattr(request.user, 'claims') and DeleteForumThreadClaim in request.user.claims


class CanDeleteThreadReplyClaim(permissions.BasePermission):
    message = 'Delete Thread Reply are not allowed.'
    
    def has_permission(self, request, view):
        return hasattr(request.user, 'claims') and DeleteThreadReplyClaim in request.user.claims
    