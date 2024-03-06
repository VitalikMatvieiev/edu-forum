from rest_framework.exceptions import NotFound
from .implementations import ForumThreadRepository, DjangoCache
from ..domain.models import ForumThread


class ForumThreadService:
    def __init__(self):
        self.repository = ForumThreadRepository()
        self.cache = DjangoCache()
    
    def get_all_threads(self):
        cache_key = "thread_list"
        thread_list = self.cache.get(cache_key)
        if thread_list is not None:
            return thread_list
        
        try:
            thread_list = self.repository.get_all_threads()
            if thread_list:
                self.cache.set(cache_key, thread_list, 60 * 5)  # Cache for 5 minutes
                return thread_list
            else:
                raise ForumThread.DoesNotExist
        except ForumThread.DoesNotExist:
            raise NotFound(detail="No forum threads found", code=404)
