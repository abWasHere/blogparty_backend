from django.contrib import admin

# Register your models here.
from .models import Party, Ticket, Venue

admin.site.register(Party)
admin.site.register(Ticket)
admin.site.register(Venue)
