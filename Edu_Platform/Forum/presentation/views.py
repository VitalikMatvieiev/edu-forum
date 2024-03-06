from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.decorators import method_decorator
from rest_framework.exceptions import NotFound
from ..repositories.implementations import ForumThreadRepository
from ..repositories.forum_service import ForumThreadService
from ..domain.models import ForumThread, ThreadReply
from ..adapters.serializers import ForumThreadSerializer, ThreadReplySerializer
from ..application.permissions import HasViewForumThreadClaim, HasViewThreadReplyClaim, CanCreateForumThreadClaim, \
    CanCreateThreadReplyClaim, CanUpdateForumThreadClaim, CanUpdateThreadReplyClaim, CanDeleteForumThreadClaim, \
    CanDeleteThreadReplyClaim


@method_decorator(cache_page(60 * 5), name='dispatch')
class ForumThreadList(generics.ListAPIView):
    serializer_class = ForumThreadSerializer
    permission_classes = [HasViewForumThreadClaim]
    
    def get_queryset(self):
        service = ForumThreadService()
        return service.get_all_threads()

  
class ForumThreadDetail(generics.RetrieveAPIView):
    queryset = ForumThread.objects.all()
    serializer_class = ForumThreadSerializer
    permission_classes = [HasViewForumThreadClaim]
    
    


class ThreadReplyList(generics.ListAPIView):
    queryset = ThreadReply.objects.all().order_by('-created_date')
    serializer_class = ThreadReplySerializer
    permission_classes = [HasViewThreadReplyClaim]


class ThreadReplyDetail(generics.RetrieveAPIView):
    queryset = ThreadReply.objects.all()
    serializer_class = ThreadReplySerializer
    permission_classes = [HasViewThreadReplyClaim]


class CreateForumThreadView(generics.CreateAPIView):
    queryset = ForumThread.objects.all()
    serializer_class = ForumThreadSerializer
    permission_classes = [CanCreateForumThreadClaim, IsAuthenticated]
    
    def get_serializer_context(self):
        context = super(CreateForumThreadView, self).get_serializer_context()
        context.update({"request": self.request})
        return context
    
    def perform_create(self, serializer):
        serializer.save()


class CreateThreadReplyView(generics.CreateAPIView):
    queryset = ThreadReply.objects.all()
    serializer_class = ThreadReplySerializer
    permission_classes = [CanCreateThreadReplyClaim, IsAuthenticated]
    
    def perform_create(self, serializer):
        thread_id = self.kwargs.get('thread_id')
        thread = generics.get_object_or_404(ForumThread, pk=thread_id)
        serializer.save(thread=thread)


class UpdateForumThreadView(generics.UpdateAPIView):
    queryset = ForumThread.objects.all()
    serializer_class = ForumThreadSerializer
    permission_classes = [CanUpdateForumThreadClaim, IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class UpdateThreadReplyView(generics.UpdateAPIView):
    queryset = ThreadReply.objects.all()
    serializer_class = ThreadReplySerializer
    permission_classes = [CanUpdateThreadReplyClaim, IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class DeleteForumThreadView(generics.DestroyAPIView):
    queryset = ForumThread.objects.all()
    serializer_class = ForumThreadSerializer
    permission_classes = [CanDeleteForumThreadClaim, IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Thread Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class DeleteThreadReplyView(generics.DestroyAPIView):
    queryset = ThreadReply.objects.all()
    serializer_class = ThreadReplySerializer
    permission_classes = [CanDeleteThreadReplyClaim, IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Reply Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
