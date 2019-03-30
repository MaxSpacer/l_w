from django.shortcuts import render
from events.models import Event
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import EventJoinForm
from .models import EventJoiner
from django.views import generic
from django.urls import reverse_lazy
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404


def events_list(request):

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)

    events = Event.objects.filter(is_active=True, publicated__lte=timezone.now()).order_by('-event_date')
    events_live = Event.objects.filter(is_active=True, format__name='Очная', publicated__lte=timezone.now()).order_by('-event_date')
    events_online = Event.objects.filter(is_active=True, format__name='Онлайн', publicated__lte=timezone.now()).order_by('-event_date')

    return render(request, 'events/events.html', locals())



def event(request, pk):
    event = Event.objects.get(id=pk)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'events/event.html', locals())


class EventJoinView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
	# model = EducationOrder
    template_name = 'events/event_join.html'
    form_class = EventJoinForm
    success_message = 'Ваша заявка принята, вскоре мы вам перезвоним.'
    # success_url = reverse_lazy('educations:education_n')
    def get_success_url(self):
        event_pk=self.kwargs['pk']
        return reverse_lazy('events:event_n', kwargs={'pk': event_pk})

    def form_valid(self, form):
        if 'referer' in self.request.session:
            referer_id = self.request.session['referer']
            user = User.objects.get(pk=referer_id)
            form.instance.referal = user.profile
        event = get_object_or_404(Event,pk=self.kwargs['pk'])
        form.instance.event = event
        return super(EventJoinView, self).form_valid(form)
