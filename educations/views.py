from django.shortcuts import render
from educations.models import Education
from django.utils import timezone
from .forms import EducationOrderForm
from .models import EducationOrder
from django.views import generic
from django.urls import reverse_lazy
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin


def education_list(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    educations = Education.objects.filter(is_active=True, publicated__lte=timezone.now()).order_by('publicated')
    return render(request, 'educations/educations.html', locals())

def education(request, education_id):
    education = Education.objects.get(id=education_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'educations/education.html', locals())

# class EduorderCreateView(generic.CreateView):
#     template_name = 'educations/create_eduorder.html'
#     form_class = EducationOrderForm
#     success_message = 'Ваша заявка принята, вскоре мы вам перезвоним'
#     success_url = reverse_lazy('educationlist_n')
#
class EduorderCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
	# model = EducationOrder
    template_name = 'educations/create_eduorder.html'
    form_class = EducationOrderForm
    success_message = 'Ваша заявка принята, вскоре мы вам перезвоним'
    success_url = reverse_lazy('educationlist_n')


	def form_valid(self, form):
        model = form.save(commit=False)
        print(type(model))


        return super(EduorderCreateView, self).form_valid(form)

	# def form_valid(self, form):
    #     self.education_id = self.kwargs['education_id']
    #     book = Book.objects.get(id=self.education_id)
    #     form.instance.book = book
    #     form.instance.language = ????
    #     form.instance.uploader = self.request.user
    #     return super(
