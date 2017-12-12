from django.contrib import admin

from .models import Event, Rsvp

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_date', 'pub_date')

admin.site.register(Event, EventAdmin)
admin.site.register(Rsvp)
