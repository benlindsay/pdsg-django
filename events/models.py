from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_date = models.DateTimeField('event date')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.event_title


class Rsvp(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rsvp_date = models.DateTimeField('rsvp date')

    def __str__(self):
        return '{}, {}'.format(self.event, self.user)


class Signin(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signin_date = models.DateTimeField('signin date')

    def __str__(self):
        return '{}, {}'.format(self.event, self.user)
