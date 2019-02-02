from django.test import TestCase, RequestFactory
from unittest import skip
#To run only one function
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from django.utils.text import slugify

from posts.models import Post
from posts.views import post_detail, post_list

User = get_user_model()

class PostAuthTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            username='abc',
            email='my@email.com',
            password = '123',
            is_staff = True
        )

    def create_post(self, title='This title'):
        return Post.objects.create(title=title)

    def test_user_auth(self):
        obj = self.create_post(title='Another New Title Test')
        #response = self.client.get(obj.get_absolute_url())
        #create the fake request
        request = self.factory.get(obj.get_absolute_url())
        request.user = self.user
        #create the response
        response = post_detail(request, slug=obj.slug)
        self.assertEqual(response.status_code, 200)

    @skip('not yet')
    def test_detail_view(self):
        obj = self.create_post(title='Another New Title Test')
        response = self.client.get(obj.get_absolute_url())
        self.assertEqual(response.status_code, 404)

    def test_empty_page(self):
        page = '/sdjfas/asdfas/asdf'
        request = self.factory.get(page)
        request.user = self.user
        response = post_list(request)
        self.assertEqual(response.status_code, 200)


