from django.urls import path
from party.views.party_views import get_post_parties
from party.views.venue_views import get_venues


urlpatterns = [
    path('', get_post_parties, name='get_post_parties_url'),
    path('venues/', get_venues, name='get_venues_url'),
]
