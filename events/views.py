from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from datetime import timedelta

from .models import Event
from .models import Rsvp
from .models import Signin
from penndsg.settings import EVENTS_SIGNIN_HOURS_BEFORE
from penndsg.settings import EVENTS_SIGNIN_HOURS_AFTER

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        """Return all events"""
        events = Event.objects.all()
        return events


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        signin_start_time = (
            context['event'].start_time -
            timedelta(hours=EVENTS_SIGNIN_HOURS_BEFORE)
        )
        signin_end_time = (
            context['event'].end_time +
            timedelta(hours=EVENTS_SIGNIN_HOURS_AFTER)
        )
        now = timezone.now()
        if now < signin_start_time or now > signin_end_time:
            context['signin_open'] = False
        else:
            context['signin_open'] = True
        context['just_added'] = False
        return context


def rsvp_success(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {'event': event}
    return render(request, 'events/rsvp-success.html', context)


def rsvp_failure(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {'event': event}
    return render(request, 'events/rsvp-failure.html', context)


def rsvp(request, pk):
    event = get_object_or_404(Event, pk=pk)

    # Redirect to the event page if this function was accessed without an
    # email POSTed
    try:
        email = request.POST['email']
    except:
        return redirect('events:detail', pk=pk)

    # Get or add user
    try:
        just_added = False
        user = User.objects.get(email=email)
    except:
        # Add email to database if not there yet
        # Usernames have to be unique, so make username email too.
        just_added = True
        user = User(username=email, email=email)
        user.save()

    try:
        rsvp = Rsvp.objects.get(user=user, event=event)
        messages.add_message(
            request,
            messages.ERROR,
            '{} has already been used to RSVP for this event'.format(email)
        )
    except:
        now = timezone.now()
        rsvp = Rsvp(user=user, event=event, rsvp_date=now)
        rsvp.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            "You have successfully RSVP'ed with {}".format(email)
        )
    return redirect('events:detail', pk=pk)

    # context = {'event': event, 'user': user, 'just_added': just_added}
    # if success:
    #     return HttpResponseRedirect(
    #         reverse('events:rsvp-success', args=(event.pk,))
    #     )
    # else:
    #     return HttpResponseRedirect(
    #         reverse('events:rsvp-failure', args=(event.pk,))
    #     )


def signin_success(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {'event': event}
    return render(request, 'events/signin-success.html', context)


def signin_failure(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {'event': event}
    return render(request, 'events/signin-failure.html', context)


def signin(request, pk):
    event = get_object_or_404(Event, pk=pk)

    # Redirect to the event page if this function was accessed without an
    # email POSTed
    try:
        email = request.POST['email']
    except:
        return redirect('events:detail', event_id=pk)

    # Get or add user
    try:
        just_added = False
        user = User.objects.get(email=email)
    except:
        # Add email to database if not there yet
        # Usernames have to be unique, so make username email too.
        just_added = True
        user = User(username=email, email=email)
        user.save()

    try:
        signin = Signin.objects.get(user=user, event=event)
        success = False
    except:
        now = timezone.now()
        signin = Signin(user=user, event=event, signin_date=now)
        signin.save()
        success = True

    context = {'event': event, 'user': user, 'just_added': just_added}
    if success:
        return HttpResponseRedirect(
            reverse('events:signin-success', args=(event.pk,))
        )
    else:
        return HttpResponseRedirect(
            reverse('events:signin-failure', args=(event.pk,))
        )
