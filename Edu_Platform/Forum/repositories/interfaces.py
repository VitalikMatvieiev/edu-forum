from abc import ABC, abstractmethod
from typing import Any, List


class IForumThreadRepository(ABC):
    @abstractmethod
    def get_all_threads(self) -> List[Any]:
        pass
    
    @abstractmethod
    def get_thread_by_id(self, thread_id: int) -> Any:
        pass


class IThreadReplyRepository(ABC):
    @abstractmethod
    def get_all_replies(self) -> List[Any]:
        pass
    
    @abstractmethod
    def get_reply_by_id(self, reply_id: int) -> Any:
        pass


class ICache(ABC):
    @abstractmethod
    def get(self, key):
        pass
    
    @abstractmethod
    def set(self, key, value, timeout=None):
        pass
    
    @abstractmethod
    def delete(self, key):
        pass
