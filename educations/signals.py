# -*- coding: utf-8 -*-

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from educations.models import EducationOrder
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404



@receiver(post_save, sender=EducationOrder)
def send_mail_on_create(sender, instance, created, **kwargs):
    if created:
        # chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        # reflink = get_random_string(4, chars) + str(instance.id)
        # Profile.objects.create(user=instance,reflink=reflink)
        context = {
		    'order_name': instance.customer_name,
		    'order_number': instance.id,
		    'order_edu': instance.education,
		    'contact_phone': instance.customer_phone,
		}
        subject = 'Заказ курса № edu-%s' % instance.id
        print(subject)
        html_message = render_to_string('includes/mail_template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'info@likwid.club'
        to = 'edu_orders@likwid.club'

        if subject and html_message and from_email:
            try:
                if send_mail(subject, html_message, from_email, [to]):
                   instance.is_emailed = True
                   instance.save()
            except BadHeaderError:

                print('Invalid header found in email')
                return HttpResponse('Invalid header found.')

            # education_order.is_emailed = True
            return HttpResponse('sended')
        else:
	        print('Make sure all fields are entered and valid.')
	        # to get proper validation errors.
			# print('wring_any_field')
	        return HttpResponse('Make sure all fields are entered and valid.')

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
