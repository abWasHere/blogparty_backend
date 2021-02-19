from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from party.models import Venue
from party.serializers import VenueSerializer


@api_view(["GET"])
def get_venues(req):
    all_venues = Venue.objects.all()
    serializer = VenueSerializer(
        all_venues, context={"request": req}, many=True
    )
    return Response(serializer.data)
