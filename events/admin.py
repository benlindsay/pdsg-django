from django.contrib.admin import ModelAdmin
from django.contrib.admin import site
from django.forms import ModelForm
from django.forms import ValidationError

from .models import Event
from .models import Rsvp
from .models import Signin


# class EventForm(ModelForm):
#     class Meta:
#         model = Event

#         def clean(self):
#             start_time = self.cleaned_data.get('start_time')
#             end_time = self.cleaned_data.get('end_time')
#             if start_time > end_time:
#                 raise ValidationError("Dates are incorrect")
#             return self.cleaned_data


class EventAdmin(ModelAdmin):
    # form = EventForm
    list_display = ('title', 'start_time', 'end_time', 'pub_date')


site.register(Event, EventAdmin)
site.register(Rsvp)
site.register(Signin)
