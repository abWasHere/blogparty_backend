from datetime import datetime
import pytz

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from party.models import Party, Venue, Ticket
from party.serializers import PartySerializer, VenueSerializer

client = Client()  # initialize the APIClient app


class TestViews(TestCase):
    def setUp(self):
        self.date1 = datetime(2021, 5, 11, 20, 30, 0, 0, tzinfo=pytz.UTC)
        self.venue1 = Venue.objects.create(
            name="The Club", city="Paris", zip_code="75001", capacity=30
        )
        self.party1 = Party.objects.create(
            title="Party1 Project X",
            organizer="Audrey",
            date=self.date1,
            venue=self.venue1,
        )

        self.url1 = reverse("get_post_parties_url")
        self.response1 = client.get(self.url1)

        self.url2 = reverse("get_venues_url")
        self.response2 = client.get(self.url2)

    # get api response w/ status ok
    def test_get_post_parties_GET_status_ok(self):
        self.assertEqual(self.response1.status_code, status.HTTP_200_OK)

    # get data from db
    def test_get_post_parties_GET_data(self):
        parties = Party.objects.all()
        serializer1 = PartySerializer(parties, many=True)

        self.assertEqual(self.response1.data, serializer1.data)

    # post data
    def test_get_post_parties_POST_status_ok(self):
        pass

    def test_get_venues_GET_data(self):
        venues = Venue.objects.all()
        serializer2 = VenueSerializer(venues, many=True)

        self.assertEqual(self.response2.data, serializer2.data)

    def test_get_venues_GET_status_ok(self):
        self.assertEqual(self.response2.status_code, status.HTTP_200_OK)
