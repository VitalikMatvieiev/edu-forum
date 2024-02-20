from rest_framework import serializers
from ..domain.models import ForumThread, ThreadReply


class ForumThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumThread
        fields = ['id', 'course_id', 'title', 'content']
        extra_kwargs = {
            'created_date': {'read_only': True},
            'title': {'required': True, 'max_length': 200},
            'content': {'required': True}
        }
    
    def create(self, validated_data):
        return ForumThread.objects.create(**validated_data)


class ThreadReplySerializer(serializers.ModelSerializer):
    thread_id = serializers.SerializerMethodField()
    
    class Meta:
        model = ThreadReply
        fields = ['id', 'thread_id', 'user_id', 'content']
        extra_kwargs = {
            'created_date': {'read_only': True},
        }
    
    def get_thread_id(self, obj):
        return obj.thread.id