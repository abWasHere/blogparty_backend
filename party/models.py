from django.db import models


class Party(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    organizer = models.CharField(max_length=50, null=False, blank=False)
    # organizer = models.ForeignKey("User", on_delete=models.CASCADE)
    date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=False, blank=False
    )
    is_canceled = models.BooleanField(default=False)
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE)

    @property
    def tickets_sold(self):
        total_tickets = Ticket.objects.filter(party=self)
        return total_tickets.count()

    @property
    def tickets_left(self):
        party_venue = Venue.objects.get(id=self.venue.id)
        return party_venue.capacity - self.tickets_sold

    @property
    def is_sold_out(self):
        if self.tickets_left == 0:
            return True
        return False

    def sell_tickets(self, buyer_id, amount):
        if self.tickets_left >= amount and self.is_canceled is False:
            for n in range(amount):
                new_ticket = Ticket.objects.create(party=self, owner=buyer_id)
                new_ticket.save()
        else:
            raise Exception(
                "Only {} tickets available. Sorry.".format(self.tickets_left)
            )

    def cancel(self):
        self.is_canceled = True


class Ticket(models.Model):
    party = models.ForeignKey("Party", on_delete=models.CASCADE)
    owner = models.PositiveIntegerField(blank=False, null=False)
    # owner = models.ForeignKey("User", on_delete=models.CASCADE)


class Venue(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=50, blank=True, null=True)
    capacity = models.PositiveIntegerField(blank=False, null=False)

    @property
    def is_online(self):
        if self.city is None and self.zip_code is None:
            return True
        return False
