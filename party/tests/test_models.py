from datetime import datetime
import pytz

from django.test import TestCase

from party.models import Party, Ticket, Venue


class TestModels(TestCase):
    def setUp(self):
        self.date1 = datetime(2021, 5, 11, 20, 30, 0, 0, tzinfo=pytz.UTC)
        self.venue1 = Venue.objects.create(
            name="The Club", city="Paris", zip_code="75001", capacity=30
        )
        self.venue2 = Venue.objects.create(name="The Club", capacity=100)
        self.party1 = Party.objects.create(
            title="Party1 Project X",
            organizer="Audrey",
            date=self.date1,
            venue=self.venue1,
        )
        self.party2 = Party.objects.create(
            title="party2 is going to be canceled",
            organizer="Robot",
            date=self.date1,
            venue=self.venue2,
        )

    def test_venue_is_online(self):

        self.assertEqual(self.venue1.is_online, False)
        self.assertEqual(self.venue1.city, "Paris")
        self.assertEqual(self.venue2.is_online, True)

    def test_party_create(self):

        self.assertEqual(self.party1.title, "Party1 Project X")
        self.assertEqual(self.party1.venue, self.venue1)
        self.assertEqual(self.party1.date, self.date1)

    def test_party_is_assigned_slug_on_create(self):
        self.assertEqual(self.party1.slug, "party1-project-x")

    def test_party_cancelation(self):
        self.party2.cancel()

        self.assertEqual(self.party2.is_canceled, True)
        self.assertEqual(self.party1.is_canceled, False)

    def test_party_sell_tickets(self):

        # buyer 1 gets 2 tickets for party 1
        buyer1 = {"buyer_name": "Joe", "id": 12}
        amount1 = 2
        rest1 = 28
        self.party1.sell_tickets(buyer1["id"], amount1)

        self.assertEqual(self.party1.tickets_sold, amount1)
        self.assertEqual(self.party1.tickets_left, rest1)

        # buyer 2 gets 0 tickets for party 2
        buyer2 = {"buyer_name": "Jane", "id": 33}
        amount2 = 0
        self.party1.sell_tickets(buyer2["id"], amount2)

        self.assertEqual(self.party1.is_sold_out, False)
        self.assertEqual(self.party2.tickets_sold, 0)

        # buyer 3 gets 100 tickets for party 3
        buyer3 = {"buyer_name": "Jane", "id": 33}
        amount3 = 100

        with self.assertRaises(Exception):
            self.party1.sell_tickets(buyer3["id"], amount3)

            # FIXME: this should not pass :
            self.assertEqual(
                Exception, f"Only {rest1} tickets avlable. Sorry."
            )

    def test_tickets_creation(self):
        buyer1 = {"buyer_name": "Joe", "id": 12}
        amount1 = 11
        self.party1.sell_tickets(buyer1["id"], amount1)

        all_tickets = Ticket.objects.all().count()

        self.assertEquals(all_tickets, 11)
