from django.urls import path
from .views import ForumThreadList, ForumThreadDetail, ThreadReplyList, ThreadReplyDetail

urlpatterns = [
    path('threads/', ForumThreadList.as_view(), name='thread-list'),
    path('threads/<int:pk>/', ForumThreadDetail.as_view(), name='thread-detail'),
    path('threads/replies/', ThreadReplyList.as_view(), name='reply-list'),
    path('threads/<int:pk>/replies/', ThreadReplyDetail.as_view(), name='reply-detail')
]