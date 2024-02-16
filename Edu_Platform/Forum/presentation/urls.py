from django.urls import path
from .views import ThreadList, ThreadDetail

urlpatterns = [
    path('threads/', ThreadList.as_view(), name='thread-list'),
    path('threads/<int:pk>/', ThreadDetail.as_view(), name='thread-detail'),
]