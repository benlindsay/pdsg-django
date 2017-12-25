from django.conf.urls import url

from .views import IndexView
from .views import EventDetailView
from .views import rsvp
from .views import rsvp_success
from .views import rsvp_failure
from .views import signin
from .views import signin_success
from .views import signin_failure

app_name = 'events'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', EventDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/rsvp/$', rsvp, name='rsvp'),
    url(r'^(?P<pk>[0-9]+)/rsvp-success/$', rsvp_success, name='rsvp-success'),
    url(r'^(?P<pk>[0-9]+)/rsvp-failure/$', rsvp_failure, name='rsvp-failure'),
    url(r'^(?P<pk>[0-9]+)/signin/$', signin, name='signin'),
    url(r'^(?P<pk>[0-9]+)/signin-success/$', signin_success, name='signin-success'),
    url(r'^(?P<pk>[0-9]+)/signin-failure/$', signin_failure, name='signin-failure'),
]
