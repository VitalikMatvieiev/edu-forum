from rest_framework import generics
from ..domain.models import ForumThread, ThreadReply
from ..adapters.serializers import ForumThreadSerializer, ThreadReplySerializer
from ..application.permissions import HasViewForumThreadClaim


class ThreadList(generics.ListAPIView):
    queryset = ForumThread.objects.all()
    serializer_class = ForumThreadSerializer
    permission_classes = [HasViewForumThreadClaim]


class ThreadDetail(generics.RetrieveAPIView):
    queryset = ForumThread.objects.all()
    serializer_class = ForumThreadSerializer
    permission_classes = [HasViewForumThreadClaim]



    
