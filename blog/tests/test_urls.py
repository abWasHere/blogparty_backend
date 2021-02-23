from django.test import TestCase
from django.urls import reverse, resolve

from ..views import get_post_blogs, get_delete_put_blog


# get the correct view
class TestUrls(TestCase):
    def setUp(self):
        self.url1 = reverse("get_post_blogs_url")
        self.url2 = reverse("get_delete_put_blog_url", args=['1'])

    def test_get_post_blogs_url_resolves(self):
        view = resolve(self.url1)

        self.assertEqual(view.func, get_post_blogs)

    def test_get_delete_put_blog_url_resolves(self):
        view = resolve(self.url2)

        self.assertEqual(view.func, get_delete_put_blog)
