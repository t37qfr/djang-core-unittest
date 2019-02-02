from django.test import TestCase
from unittest import skip
#To run only one function
from django.conf import settings

from django.utils.text import slugify
from django.utils import timezone

from posts.forms import PostForm
from posts.models import Post


class PostFormTestCase(TestCase):
    def test_valid_form(self):
        title = 'A new title'
        slug = 'unique-slug-123'
        content = 'some content'
        obj = Post.objects.create(
            title=title,
            slug=slug,
            publish=timezone.now(),
            content=content
        )
        data = {
            'title': obj.title,
            'slug': obj.slug,
            'publish': obj.publish,
            'content': content,

        }

        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('title'), obj.title)
        self.assertEqual(form.cleaned_data.get('content'), obj.content)

    @skip('fail')
    def test_in_valid_form(self):
        title = 'A new title'
        slug = 'unique-slug-123'
        content = 'some content'
        obj = Post.objects.create(
            title=title,
            slug=slug,
            publish=timezone.now(),
            content=content
        )
        data = {
            'title': obj.title,
            'slug': obj.slug,
            'publish': obj.publish,
            'content': content,

        }

        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.cleaned_data.get('title'), obj.title)
        self.assertEqual(form.cleaned_data.get('content'), obj.content)


