from django.shortcuts import render
from events.models import Event
from django.utils import timezone


def events_list(request):

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)

    # events = EventImage.objects.filter(is_active=True, event__publicated__lte=timezone.now()).order_by("publicated")  event__name = '134'
    events = Event.objects.filter(is_active=True, publicated__lte=timezone.now()).order_by('-publicated')
    # events = ListView.as_view(queryset=Event.objects.filter(is_active=True, publicated__lte=date.datetime.now() ).order_by("publicated"),template_name="events/events_cards.html")),
    print(events)
    return render(request, 'events/events.html', locals())


def event(request, event_id):
    event = Event.objects.get(id=event_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'events/event.html', locals())
