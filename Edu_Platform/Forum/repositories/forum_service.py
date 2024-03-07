from rest_framework.exceptions import NotFound
from .implementations import ForumThreadRepository, ThreadReplyRepository, DjangoCache
from ..domain.models import ForumThread, ThreadReply


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
    
    def get_thread_by_id(self, thread_id):
        cache_key = f'thread_{thread_id}'
        thread = self.cache.get(cache_key)
        if not thread:
            thread = self.repository.get_thread_by_id(thread_id)
            self.cache.set(cache_key, thread, 60 * 5)
        return thread


class ThreadReplyService:
    def __init__(self):
        self.repository = ThreadReplyRepository()
        self.cache = DjangoCache()
    
    def get_all_replies(self):
        cache_key = "replies_list"
        replies_list = self.cache.get(cache_key)
        
        if replies_list is not None:
            return replies_list
        
        replies_list = self.repository.get_all_replies()
        self.cache.set(cache_key, replies_list, 60 * 5)  # Cache for 5 minutes
        return replies_list
    
    def get_reply_by_id(self, reply_id):
        cache_key = f'thread_reply_{reply_id}'
        reply = self.cache.get(cache_key)
        
        if not reply:
            reply = self.repository.get_reply_by_id(reply_id)
            self.cache.set(cache_key, reply, 60 * 5)
        return reply
