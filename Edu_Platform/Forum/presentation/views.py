from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..domain.models import ForumThread, ThreadReply
from ..adapters.serializers import ForumThreadSerializer, ThreadReplySerializer
from ..application.permissions import HasViewForumThreadClaim, HasViewThreadReplyClaim, CanCreateForumThreadClaim


class ForumThreadList(generics.ListAPIView):
    queryset = ForumThread.objects.all().order_by('-created_date')
    serializer_class = ForumThreadSerializer
    permission_classes = [HasViewForumThreadClaim]


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
    
    def perform_create(self, serializer):
        serializer.save()

    
