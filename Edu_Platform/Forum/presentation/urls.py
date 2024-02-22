from django.urls import path
from .views import ForumThreadList, ForumThreadDetail, ThreadReplyList, ThreadReplyDetail, CreateForumThreadView, \
    CreateThreadReplyView

urlpatterns = [
    path('threads/', ForumThreadList.as_view(), name='thread-list'),
    path('threads/<int:pk>/', ForumThreadDetail.as_view(), name='thread-detail'),
    path('threads/replies/', ThreadReplyList.as_view(), name='reply-list'),
    path('threads/<int:pk>/replies/', ThreadReplyDetail.as_view(), name='reply-detail'),
    path('threads/create/', CreateForumThreadView.as_view(), name='create-thread'),
    path('threads/<int:thread_id>/replies/create/', CreateThreadReplyView.as_view(), name='create-reply'),
]
