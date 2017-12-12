from django.conf.urls import url

from .views import IndexView, EventDetailView, rsvp, rsvp_success, rsvp_failure

app_name = 'events'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', EventDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/rsvp/$', rsvp, name='rsvp'),
    url(r'^(?P<pk>[0-9]+)/rsvp-success/$', rsvp_success, name='rsvp-success'),
    url(r'^(?P<pk>[0-9]+)/rsvp-failure/$', rsvp_failure, name='rsvp-failure'),
]
