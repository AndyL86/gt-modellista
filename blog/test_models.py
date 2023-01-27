from .models import Comment, Thread
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.utils import timezone
from django.urls import reverse
import base64
import tempfile


Author = get_user_model()

class TestModels(TestCase):


    def setUp(self):
        self.user = Author.objects.create_user(
            username='testmember',
            password='testingtest'
        )
        self.client.login(username='testmember', password='testingtest')
        self.thread = Thread.objects.create(
            author=self.user,
            year='9999',
            make='Test',
            model='test',
            story='test story',
            modifications='test modifications',
            post_date=timezone.now(),
            slug='test-slug',
        )
        self.comment = Comment.objects.create(
            thread=self.thread,
            name="test-instance",
            body='test comment',
        )
