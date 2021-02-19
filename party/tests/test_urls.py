from django.test import TestCase, Client
from django.urls import reverse, resolve

from party.urls import get_post_parties_url, get_venues_url

# initialize the APIClient app
client = Client()


class TestUrls(TestCase):
    def setUp(self):

        pass

    def test_get_post_parties_url(self):
        """
        GET ALL PARTIES
        """
        # get api response
        url = reverse('get_post_parties_url')
        response = client.get(url)

        # get data from db


    def test_venue_list_url(self):
        pass    