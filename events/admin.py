from django.contrib import admin

from .models import Event
from .models import Rsvp
from .models import Signin

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_date', 'pub_date')

admin.site.register(Event, EventAdmin)
admin.site.register(Rsvp)
admin.site.register(Signin)
