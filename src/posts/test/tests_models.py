from django.test import TestCase
from unittest import skip
#To run only one function
from django.conf import settings

from django.utils.text import slugify

from posts.models import Post


class PostModelTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            title='A new title',
            slug='unique-slug-123'
        )

    def create_post(self, title='This title'):
        return Post.objects.create(title=title)

    @skip('fail')
    def test_post_title(self):
        obj = Post.objects.get(slug='unique-slug-123')
        self.assertEqual(obj.title, 'A new title')
        self.assertTrue(obj.content !="")

    def test_post_slug(self):
        title1 = 'another abc'
        title2 = 'another abc2'
        slug1 = slugify(title1)
        slug2 = slugify(title2)
        obj1 = self.create_post(title=title1)
        obj2 = self.create_post(title=title2)
        self.assertEqual(obj1.slug, slug1)
        self.assertEqual(obj2.slug,slug2)

    def test_post_qs(self):
        title = 'another abc'
        obj1 = self.create_post(title=title)
        obj2 = self.create_post(title=title)
        qs = Post.objects.filter(title=title)
        self.assertEqual(qs.count(), 2)

        qs2 = Post.objects.filter(slug=obj1.slug)
        self.assertEqual(qs2.count(),  1)

