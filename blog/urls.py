from django.urls import path, re_path

from .views import get_post_blogs
from .views import get_delete_put_blog


urlpatterns = [
    path("", get_post_blogs, name="get_post_blogs_url"),
    re_path(
        r"(?P<pk>[0-9]+)$", get_delete_put_blog, name="get_delete_put_blog_url"
    ),
]

"""
Named Capture Group pk (?P<pk>[0-9]+):
Match a single character present in the list below [0-9]+

+ Quantifier : Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
0-9 a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
$ asserts position at the end of a line
"""
