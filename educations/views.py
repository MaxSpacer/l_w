from django.shortcuts import get_object_or_404
from django.shortcuts import render
from educations.models import Education
from django.utils import timezone
from .forms import EducationOrderForm
from .models import EducationOrder
from django.views import generic
from django.urls import reverse_lazy
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


def education_list(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    educations = Education.objects.filter(is_active=True, publicated__lte=timezone.now()).order_by('category')
    return render(request, 'educations/educations.html', locals())

def education(request, pk):
    # education = Education.objects.get(id=pk)
    education = get_object_or_404(Education, id=pk)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'educations/education.html', locals())


class EduorderCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
	# model = EducationOrder
    template_name = 'educations/create_eduorder.html'
    form_class = EducationOrderForm
    success_message = 'Ваша заявка принята, вскоре мы вам перезвоним.'
    # success_url = reverse_lazy('educations:education_n')
    def get_success_url(self):
        educations_pk=self.kwargs['pk']
        return reverse_lazy('educations:education_n', kwargs={'pk': educations_pk})

    def form_valid(self, form):
        if 'referer' in self.request.session:
            referer_id = self.request.session['referer']
            user = User.objects.get(pk=referer_id)
            # form.instance.referal = user.profile
            form.instance.referal = user.profile
        education = get_object_or_404(Education,pk=self.kwargs['pk'])
        form.instance.education = education
        # f=form.cleaned_data
        # # for k, v in form.cleaned_data.items():
        #     # print(k, '=', v)
        # # print(f.items())
        # print(f.get('customer_phone'))
        # print(education.name)
        # for key, value in f:
        #     print("%s = %s" % (key, value))
                # form.save()

        # if form.instance.is_emailed == False:
        #                 context = {
        #                 'order_name': form.instance.customer_name,
        #                 'order_number': instance.pk,
        #                 'order_edu': form.instance.education,
        #                 'contact_phone': form.instance.customer_phone,
        #                 }
        #             subject = 'Заказ курса № edu-%s' % instance.pk
        #             print(subject)
        #             html_message = render_to_string('includes/mail_template.html', context)
        #             plain_message = strip_tags(html_message)
        #             from_email = 'info@likwid.club'
        #             to = 'edu_orders@likwid.club'
        #
        #             if subject and html_message and from_email:
        #                 try:
        #                     if send_mail(subject, html_message, from_email, [to]):
        #                         EducationOrder.objects.filter(pk=instance.pk).update(is_emailed=True)
        #
        #                        # education_order = get_object_or_404(EducationOrder, id=instance.id)
        #                        # education_order.update(is_emailed=True)
        #                 except BadHeaderError:
        #                     print('Invalid header found in email')
        #                     return HttpResponse('Invalid header found.')
        #
        #                 # education_order.is_emailed = True
        #                 return HttpResponse('sended')
        #             else:
        #     	        print('Make sure all fields are entered and valid.')
        #     	        # to get proper validation errors.
        #     			# print('wring_any_field')
        #     	        # return HttpResponse('Make sure all fields are entered and valid.')
        #     if send_email(f, f):
        #
        #         print('done mail')
        #         form.instance.is_emailed = True
            # if send_email(form.cleaned_data):
        # form.instance.is_emailed = True
        # form.instance.is_emailed = True
        # form.save()
        return super(EduorderCreateView, self).form_valid(form)
