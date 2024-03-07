from rest_framework import serializers
from ..domain.models import ForumThread, ThreadReply


class ForumThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumThread
        fields = ['id', 'course_id', 'title', 'content', 'created_date']
        read_only_fields = ['id', 'created_date']
        extra_kwargs = {
            'title': {'required': True, 'max_length': 200},
            'content': {'required': True},
        }
    
    def __init__(self, *args, **kwargs):
        super(ForumThreadSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == 'POST':
            # Only set course_id as required if this is a POST request
            self.fields['course_id'] = serializers.IntegerField(required=True)
        else:
            # For other methods (PUT, PATCH, etc.), course_id is read_only
            self.fields['course_id'] = serializers.IntegerField(read_only=True)
    
    def create(self, validated_data):
        return ForumThread.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class ThreadReplySerializer(serializers.ModelSerializer):
    thread_id = serializers.SerializerMethodField()
    
    class Meta:
        model = ThreadReply
        fields = ['id', 'thread_id', 'user_id', 'content', 'created_date']
        read_only_fields = ['id', 'created_date', 'thread_id']
        extra_kwargs = {
            'content': {'required': True, 'max_length': 5000},
        }
    
    def get_thread_id(self, obj):
        return obj.thread.id
    
    def create(self, validated_data):
        return ThreadReply.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
    
    def validate_content(self, value):
        if value.strip() == '':
            raise serializers.ValidationError("Content cannot be empty or whitespace.")
        return value
