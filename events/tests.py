from datetime import timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone

from .models import Event
from .models import Rsvp
from .models import Signin


class EventTests(TestCase):

    def setUp(self):
        self.event = Event(
            title='Awesome Event',
            start_time=timezone.now(),
            end_time=timezone.now() + timedelta(hours=1),
            pub_date=timezone.now()
        )
        email='test@email.com'
        self.event.save()

        self.user = User(username=email, email=email)
        self.user.save()


    def test_event_creation_with_end_before_start_fails(self):
        self.assertRaises(
            ValidationError,
            Event(
                title='Bad Event',
                start_time=timezone.now(),
                end_time=timezone.now() - timedelta(minutes=1),
                pub_date=timezone.now()
            ).save
        )


    def test_duplicate_rsvp_fails(self):
        rsvp = Rsvp(event=self.event, user=self.user, rsvp_date=timezone.now())
        rsvp.save()
        self.assertRaises(
            IntegrityError,
            Rsvp(
                event=self.event,
                user=self.user,
                rsvp_date=timezone.now()
            ).save
        )


    def test_duplicate_signin_fails(self):
        signin = Signin(
            event=self.event, user=self.user, signin_date=timezone.now()
        )
        signin.save()
        self.assertRaises(
            IntegrityError,
            Signin(
                event=self.event,
                user=self.user,
                signin_date=timezone.now()
            ).save
        )
