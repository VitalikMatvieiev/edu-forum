from rest_framework import serializers
from ..domain.models import ForumThread, ThreadReply


class ForumThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumThread
        fields = ['course_id', 'title', 'content']
        extra_kwargs = {
            'created_date': {'read_only': True},
        }


class ThreadReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadReply
        fields = ['thread', 'user_id', 'content']
        extra_kwargs = {
            'created_date': {'read_only': True},
        }
        