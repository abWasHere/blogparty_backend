from django.test import TestCase

from blog.models import Blog, Tag


class TestBlog(TestCase):
    def setUp(self):
        self.blog_audrey = Blog.objects.create(
            title="My Life Blog",
            content="This is a blog about my life and parties on the internet.",
            user="Audrey",
        )
        self.tag1 = Tag.objects.create(blog=self.blog_audrey, name="lifestyle")
        self.tag2 = Tag.objects.create(blog=self.blog_audrey, name="testing")
        self.tag3 = Tag.objects.create(blog=self.blog_audrey, name="django")

    def test_blog_creation(self):
        created_blog = Blog.objects.first()

        self.assertEqual(created_blog, self.blog_audrey)

    def test_tag_creation(self):
        self.assertEqual(self.tag1.blog, self.blog_audrey)
        self.assertEqual(self.tag1.name, "lifestyle")
        self.assertEqual(self.tag3.name, "django")

    def test_blog_gets_tags(self):
        blog_tags = Tag.objects.filter(blog=self.blog_audrey)

        self.assertEqual(blog_tags.count(), 3)
