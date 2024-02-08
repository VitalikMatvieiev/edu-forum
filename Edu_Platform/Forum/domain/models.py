from django.db import models
from django.utils import timezone


class ForumThread(models.Model):
    course_id = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.title} [Course ID: {self.course_id}]'


class ThreadReply(models.Model):
    thread = models.ForeignKey(
        ForumThread,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    user_id = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Reply by User {self.user_id} on "{self.thread.title}"'
        
    
    
    
