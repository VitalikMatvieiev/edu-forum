from rest_framework import permissions

ViewForumThreadClaim = 'ViewForumThreadClaim'


class HasViewForumThreadClaim(permissions.BasePermission):
    message = 'Viewing Forum Thread is not allowed.'
    
    def has_permission(self, request, view):
        return ViewForumThreadClaim in request.user.claims

    