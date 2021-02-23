import json
from rest_framework import status

from django.test import TestCase, Client
from django.urls import reverse

from ..models import Blog
from ..serializers import BlogSerializer


client = Client()  # initialize the APIClient app


class TestBlogs(TestCase):
    def setUp(self):
        self.blog_influenseuz = Blog.objects.create(
            title="my life on the internet",
            content="I like to share everything about me on the internet.",
            user="Influenseuz77",
        )
        self.blog_bot = Blog.objects.create(
            title="How I became a famous blogger",
            content="This is a long story.",
            user="Bot",
        )

        self.url1 = reverse("get_post_blogs_url")
        self.response1 = client.get(self.url1)

        self.url2 = reverse(
            "get_delete_put_blog_url", kwargs={"pk": self.blog_bot.pk}
        )
        self.response2 = client.get(self.url2)

        self.valid_payload1 = {
            "title": "My valid payload blog",
            "slug": "my-valid-payload-blog",
            "content": "I am valid content",
            "user": "Audrey",
        }
        self.invalid_payload1 = {
            "title": "",
            "content": 1989,
            "user": "Audrey",
        }
        self.valid_payload2 = {
            "title": "My valid payload",
            "slug": "my-valid-payload",
            "content": "",
            "user": "Audrey",
        }
        self.invalid_payload2 = {
            "title": "",
            "content": "My invalid payload content",
            "user": "Audrey",
        }

    def test_GET_all_blogs_w_status_ok(self):
        self.assertEqual(self.response1.status_code, status.HTTP_200_OK)

    def test_GET_all_blogs_w_data(self):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)

        self.assertEqual(self.response1.data, serializer.data)

    def test_GET_single_valid_blog(self):
        blog = Blog.objects.get(pk=self.blog_bot.pk)
        serializer = BlogSerializer(blog)

        self.assertEqual(self.response2.data, serializer.data)
        self.assertEqual(self.response2.status_code, status.HTTP_200_OK)

    def test_GET_single_invalid_blog(self):
        url = reverse("get_delete_put_blog_url", kwargs={"pk": 999})
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_POST_valid_blog(self):
        response = client.post(
            self.url1,
            data=json.dumps(self.valid_payload1),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_POST_invalid_blog(self):
        response = client.post(
            self.url1,
            data=json.dumps(self.invalid_payload1),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_PUT_valid_blog(self):
        response = client.put(
            self.url2,
            data=json.dumps(self.valid_payload2),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_PUT_invalid_blog(self):
        response = client.put(
            self.url2,
            data=json.dumps(self.invalid_payload2),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_DELETE_blog(self):
        response = client.delete(
            self.url2,
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_DELETE_blog(self):
        response = client.delete(
            reverse("get_delete_put_blog_url", kwargs={"pk": 999}),
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
