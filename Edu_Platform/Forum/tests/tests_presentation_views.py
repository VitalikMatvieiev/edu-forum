from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from ..domain.models import ForumThread, ThreadReply
import json


class MockUser:
    def __init__(self, claims, is_authenticated=True, identity_id=None):
        self.claims = claims
        self.is_authenticated = is_authenticated
        self.identity_id = identity_id


class APIClientWithJWT(APIClient):
    def authenticate(self, claims, identity_id=None):
        user = MockUser(claims, identity_id=identity_id)
        self.force_authenticate(user=user)


class ForumThreadAndReplyTests(APITestCase):
    client_class = APIClientWithJWT
    
    @classmethod
    def setUpTestData(cls):
        # Simulate a course_id since the Course model is not available.
        # This approach is purely for bypassing the NOT NULL constraint in tests.
        # Adjust the `course_id` value as necessary to align with your model's expectations.
        mock_course_id = 1
        cls.forum_thread = ForumThread.objects.create(title='Thread 1', content='Content 1', course_id=mock_course_id)
        cls.thread_reply = ThreadReply.objects.create(thread=cls.forum_thread, content='Reply 1')
    
    def test_ListForumThreads_ReturnsThreads_WhenUserHasViewClaim(self):
        self.client.authenticate(claims=['ViewForumThreadClaim'])
        response = self.client.get(reverse('thread-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_ViewForumThreadDetail_ReturnsThreadDetail_WhenUserHasViewClaim(self):
        self.client.authenticate(claims=['ViewForumThreadClaim'])
        response = self.client.get(reverse('thread-detail', kwargs={'pk': self.forum_thread.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.forum_thread.title, str(response.data))
    
    def test_ListThreadReplies_ReturnsReplies_WhenUserHasViewClaim(self):
        self.client.authenticate(claims=['ViewThreadReplyClaim'])
        response = self.client.get(reverse('reply-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_ViewThreadReplyDetail_ReturnsReplyDetail_WhenUserHasViewClaim(self):
        self.client.authenticate(claims=['ViewThreadReplyClaim'])
        response = self.client.get(reverse('reply-detail', kwargs={'pk': self.thread_reply.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.thread_reply.content, str(response.data))
    
    def test_CreateForumThread_CreatesThread_WhenUserHasCreateClaim(self):
        self.client.authenticate(claims=['CreateForumThreadClaim'])
        data = {'title': 'New Thread', 'content': 'New content', 'course_id': 1}
        response = self.client.post(reverse('create-thread'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ForumThread.objects.count(), 2)
    
    def test_CreateThreadReply_CreatesReply_WhenUserHasCreateClaim(self):
        self.client.authenticate(claims=['CreateThreadReplyClaim'])
        data = {'content': 'New reply content', 'thread': self.forum_thread.pk}
        response = self.client.post(reverse('create-reply', kwargs={'thread_id': self.forum_thread.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ThreadReply.objects.count(), 2)
