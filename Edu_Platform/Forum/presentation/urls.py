from django.urls import path
from .views import ForumThreadList, ForumThreadDetail, ThreadReplyList, ThreadReplyDetail, CreateForumThreadView, \
    CreateThreadReplyView, UpdateForumThreadView, UpdateThreadReplyView, DeleteForumThreadView, DeleteThreadReplyView

urlpatterns = [
    path('forum-threads/', ForumThreadList.as_view(), name='thread-list'),
    path('forum-threads/<int:pk>/', ForumThreadDetail.as_view(), name='thread-detail'),
    path('forum-threads/replies/', ThreadReplyList.as_view(), name='reply-list'),
    path('forum-threads/replies/<int:pk>/', ThreadReplyDetail.as_view(), name='reply-detail'),
    path('forum-threads/create/', CreateForumThreadView.as_view(), name='create-thread'),
    path('forum-threads/replies/create/<int:thread_id>/', CreateThreadReplyView.as_view(), name='create-reply'),
    path('forum-threads/update/<int:pk>/', UpdateForumThreadView.as_view(), name='update-thread'),
    path('forum-threads/replies/update/<int:pk>/', UpdateThreadReplyView.as_view(), name='update-reply'),
    path('forum-threads/delete/<int:pk>/', DeleteForumThreadView.as_view(), name='delete-thread'),
    path('forum-threads/replies/delete/<int:pk>/', DeleteThreadReplyView.as_view(), name='delete-reply')
]
