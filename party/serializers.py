from rest_framework import serializers
from .models import Party, Venue, Ticket


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = (
            "pk",
            "title",
            "slug",
            "organizer",
            "date",
            "is_canceled",
            "venue",
        )


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = (
            "pk",
            "name",
            "city",
            "zip_code",
            "capacity",
        )


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "pk",
            "party",
            "owner"
        )
