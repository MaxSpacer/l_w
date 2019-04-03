from django.shortcuts import get_object_or_404
from django.shortcuts import render
from investions.models import Investion
from django.utils import timezone
from .forms import InvestionOrderForm
from .models import InvestionOrder
from django.views import generic
from django.urls import reverse_lazy
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


def investion_list(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    # investions = investion.objects.filter(is_active=True, publicated__lte=timezone.now()).order_by('-publicated')
    investions_big = Investion.objects.filter(is_active=True, format__name='>30%', publicated__lte=timezone.now()).order_by('-publicated')
    investions_medium = Investion.objects.filter(is_active=True, format__name='10-12%', publicated__lte=timezone.now()).order_by('-publicated')
    investions_small = Investion.objects.filter(is_active=True, format__name='10%', publicated__lte=timezone.now()).order_by('-publicated')
    return render(request, 'investions/investions.html', locals())

def investion(request, pk):
    # investion = investion.objects.get(id=pk)
    investion = get_object_or_404(Investion, id=pk)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'investions/investion.html', locals())


class InvorderCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
	# model = investionOrder
    template_name = 'investions/create_eduorder.html'
    form_class = InvestionOrderForm
    success_message = 'Ваша заявка принята, вскоре мы вам перезвоним.'
    # success_url = reverse_lazy('investions:investion_n')
    def get_success_url(self):
        investions_pk=self.kwargs['pk']
        return reverse_lazy('investions:investion_n', kwargs={'pk': investions_pk})

    def form_valid(self, form):
        if 'referer' in self.request.session:
            referer_id = self.request.session['referer']
            user = User.objects.get(pk=referer_id)
            # form.instance.referal = user.profile
            form.instance.referal = user.profile
        investion = get_object_or_404(Investion,pk=self.kwargs['pk'])
        form.instance.investion = investion

        return super(EduorderCreateView, self).form_valid(form)
