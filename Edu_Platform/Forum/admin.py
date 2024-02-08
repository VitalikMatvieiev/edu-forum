from django.contrib import admin
from .domain.models import ForumThread, ThreadReply

admin.site.register(ForumThread)
admin.site.register(ThreadReply)
