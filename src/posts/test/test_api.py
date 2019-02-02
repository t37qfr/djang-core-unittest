from rest_framework.test import APIRequestFactory, force_authenticate

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from unittest import skip
from django.utils import timezone

from posts.api.views import (
    PostCreateAPIView,
    PostDeleteAPIView,
    PostDetailAPIView,
    PostListAPIView,
    PostUpdateAPIView,
    )

from posts.models import Post

User = get_user_model()

class PostApiTest(TestCase):
    def setUp(self):
        self.data = {
            'title': 'some',
            'content':'con',
            'publish':timezone.now().date()
        }
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
           username='abc',
           email='my@email.com',
           password='123',
           is_staff=True
        )

    def create_post(self, title='This title'):
        return Post.objects.create(title=title)

    def test_get_data(self):
        list_url = reverse('posts-api:list')
        obj = self.create_post()
        detail_url = reverse('posts-api:detail', kwargs={'slug': obj.slug})

        request = self.factory.get(list_url)
        response = PostListAPIView.as_view()(request, slug=obj.slug)
        self.assertEqual(response.status_code, 200)

    def test_post_data(self):
        create_url = reverse('posts-api:create')

        request = self.factory.post(create_url, data=self.data)
        force_authenticate(request, user=self.user)
        response = PostCreateAPIView.as_view()(request)
        self.assertEqual(response.status_code, 201)
