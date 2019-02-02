from django.test import TestCase
from unittest import skip
#To run only one function
from django.conf import settings

from django.utils.text import slugify

from posts.models import Post


class PostViewTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            title='A new title',
            slug='unique-slug-123'
        )

    def create_post(self, title='This title'):
        return Post.objects.create(title=title)

    def test_detail_view(self):
        obj = self.create_post(
            title='Another New Title Test'
        )
        response = self.client.get(obj.get_absolute_url())
        self.assertEqual(response.status_code, 200)


