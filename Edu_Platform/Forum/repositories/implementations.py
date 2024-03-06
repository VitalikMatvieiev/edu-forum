from django.core.cache import cache
from .interfaces import IForumThreadRepository, ICache
from ..domain.models import ForumThread


class ForumThreadRepository(IForumThreadRepository):
    def get_all_threads(self):
        return ForumThread.objects.all()
    
    def get_thread_by_id(self, thread_id: int):
        return ForumThread.objects.get(pk=thread_id)
    

class DjangoCache(ICache):
    def get(self, key):
        return cache.get(key)
    
    def set(self, key, value, timeout=None):
        cache.set(key, value, timeout)
        
    def delete(self, key):
        cache.delete(key)