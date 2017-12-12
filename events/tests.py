# import datetime

# from django.utils import timezone
# from django.test import TestCase

# from .models import Event, Rsvp
# from django.contrib.auth.models import User

# def create_user(email):
#     u = User(username=email, email=email)
#     u.save()
#     return u

# def create_event(event_title, event_date=None, pub_date=None):
#     if event_date is None:
#         event_date = timezone.now() + datetime.timedelta(days=1)
#     if pub_date is None:
#         pub_date = timezone.now()
#     e = Event(
#         event_title=event_title, event_date=event_date, pub_date=pub_date
#     )
#     e.save()
#     return e

# class RsvpModelTests(TestCase):

#     def test_multiple_entries_for_same_user_and_event(self):
#         """
#         a duplicate rsvp should alter the original one instead of creating a
#         new one
#         """
#         u = create_user('test@fake.com')
#         e = create_event('Fake Event')
#         rsvp_1 = Rsvp(user=u, event=e)
