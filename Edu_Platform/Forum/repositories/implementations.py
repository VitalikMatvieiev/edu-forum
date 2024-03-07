from typing import List, Any

from django.core.cache import cache
from .interfaces import IForumThreadRepository, IThreadReplyRepository, ICache
from ..domain.models import ForumThread, ThreadReply


class ForumThreadRepository(IForumThreadRepository):
    def get_all_threads(self) -> List[Any]:
        return ForumThread.objects.all()
    
    def get_thread_by_id(self, thread_id: int) -> Any:
        return ForumThread.objects.get(pk=thread_id)


class ThreadReplyRepository(IThreadReplyRepository):
    def get_all_replies(self) -> List[Any]:
        return ThreadReply.objects.all()
    
    def get_reply_by_id(self, reply_id: int) -> Any:
        return ThreadReply.objects.get(pk=reply_id)


class DjangoCache(ICache):
    def get(self, key):
        return cache.get(key)
    
    def set(self, key, value, timeout=None):
        cache.set(key, value, timeout)
    
    def delete(self, key):
        cache.delete(key)
