from django.db import models


class Party(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    organizer = models.CharField(max_length=50, null=False, blank=False)
    # organizer = models.ForeignKey()
    date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=False, blank=False
    )
    # FIXME: venue_id = models.ForeignKey(...)
    is_canceled = models.BooleanField(default=False)

    @property
    def tickets_sold(self):
        total_tickets = Ticket.objects.filter(party_id=self.id)  # or pk ???
        return total_tickets.count()  # or len ?

    @property
    def tickets_left(self):
        party_venue = Venue.objects.filter(party_id=self.id)
        return party_venue.capacity - self.tickets_sold

    @property
    def is_sold_out(self):
        if self.tickets_left == 0:
            return True
        return False

    def sell_tickets(self, buyer, amount):

        if self.tickets_left >= amount and self.is_canceled is False:
            # do while n<amount loop here
            for n in range(amount):
                new_ticket = Ticket.objects.create(
                    party_id=self.id, user_id=buyer.id
                )
                new_ticket.save()

    def cancel(self):
        self.is_canceled = True


class Ticket(models.model):
    pass


class Venue(models.model):
    pass
