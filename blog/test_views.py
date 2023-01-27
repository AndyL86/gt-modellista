from django.test import TestCase, Client, override_settings
from django.contrib.auth import get_user_model
from blog.models import Thread, Comment
from django.utils import timezone
from django.urls import reverse
import base64
import tempfile


Author = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        from django.core.files.uploadedfile import InMemoryUploadedFile
        from io import BytesIO
        self.user = Author.objects.create_user(
            username='testmember',
            password='testingtest'
        )
        self.client.login(username='testmember', password='testingtest')
        self.client = Client()
        self.home_url = reverse('home')
        self.about_url = reverse('about')
        self.create_thread_url = reverse('create_thread')
        self.blog_lists_url = reverse('blog_lists')
        self.my_threads_url = reverse('my_threads')
        self.thread_detail_url = reverse('thread_detail', args=['test-slug'])
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

    def test_home_get_method(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_get_method(self):
        response = self.client.get(self.about_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_thread_detail_get_method(self):
        response = self.client.get(self.thread_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thread_detail.html')

    def test_thread_detail_post_comment_method(self):
        self.client.login(username='testmember', password='testingtest')

        response = self.client.post(self.thread_detail_url, {
            'name': self.user,
            'body': 'test comment',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.thread.thread_comments.first().body,
                         'test comment')

    def test_my_threads_get_method(self):
        self.client.login(username='testmember', password='testingtest')

        response = self.client.get(self.my_threads_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_threads.html')

    def test_create_thread_get_method(self):
        self.client.login(username='testmember', password='testingtest')

        response = self.client.get(self.create_thread_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_thread.html')

    def test_create_thread_post_method(self):
        self.client.login(username='testmember', password='testingtest')

        response = self.client.post(self.create_thread_url, {
            'year':'9999',
            'make':'Test',
            'model':'test',
            'story':'test story',
            'modifications':'test modifications'
        })
