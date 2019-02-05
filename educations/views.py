from django.shortcuts import render
from educations.models import Education
from django.utils import timezone
from .forms import EducationOrderForm
from .models import EducationOrder
from django.views import generic
from django.urls import reverse_lazy
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404


def education_list(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    educations = Education.objects.filter(is_active=True, publicated__lte=timezone.now()).order_by('publicated')
    return render(request, 'educations/educations.html', locals())

def education(request, pk):
    education = Education.objects.get(id=pk)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'educations/education.html', locals())

class EduorderCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
	# model = EducationOrder
    template_name = 'educations/create_eduorder.html'
    form_class = EducationOrderForm
    success_message = 'Ваша заявка принята, вскоре мы вам перезвоним'
    # success_url = reverse_lazy('educations:education_n')
    def get_success_url(self):

        educations_pk=self.kwargs['pk']
        return reverse_lazy('educations:education_n', kwargs={'pk': educations_pk})

    def form_valid(self, form):

        self.education_id = self.kwargs['pk']
        education = get_object_or_404(Education,pk=self.kwargs['pk'])
        form.instance.education = education
        return super(EduorderCreateView, self).form_valid(form)
