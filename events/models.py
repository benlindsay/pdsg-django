from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    pub_date = models.DateTimeField('date published')

    def clean(self):
        if self.end_time < self.start_time:
            raise ValidationError(_('End time must come after start time'))

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Rsvp(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rsvp_date = models.DateTimeField('rsvp date', default=timezone.now)

    class Meta:
        unique_together = (('event', 'user'),)

    def __str__(self):
        return '{}, {}'.format(self.event, self.user)


class Signin(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signin_date = models.DateTimeField('signin date')

    class Meta:
        unique_together = (('event', 'user'),)

    def __str__(self):
        return '{}, {}'.format(self.event, self.user)
