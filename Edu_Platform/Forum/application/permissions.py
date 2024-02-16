from rest_framework import permissions

ViewForumThreadClaim = 'ViewForumThreadClaim'
ViewThreadReplyClaim = 'ViewThreadReplyClaim'


class HasViewForumThreadClaim(permissions.BasePermission):
    message = 'Viewing Forum Thread is not allowed.'
    
    def has_permission(self, request, view):
        return ViewForumThreadClaim in request.user.claims


class HasViewThreadReplyClaim(permissions.BasePermission):
    message = 'Viewing Thread Reply is not allowed.'
    
    def has_permission(self, request, view):
        return ViewThreadReplyClaim in request.user.claims