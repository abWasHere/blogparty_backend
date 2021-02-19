from django.test import TestCase, Client
from django.urls import reverse, resolve

from party.views.party_views import get_post_parties
from party.views.venue_views import get_venues


# get the correct view
class TestUrls(TestCase):
    def setUp(self):
        self.url1 = reverse("get_post_parties_url")
        self.url2 = reverse("get_venues_url")

    def test_get_post_parties_url_resolves(self):
        view = resolve(self.url1)

        self.assertEqual(view.func, get_post_parties)

    def test_get_venues_url_resolves(self):
        view = resolve(self.url2)

        self.assertEqual(view.func, get_venues)
