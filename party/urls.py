from django.urls import path
from party.views.party_views import party_list
from party.views.venue_views import venue_list


urlpatterns = [
    path('', party_list, name='party_list'),
    path('venues/', venue_list, name='venue_list'),
]
