# -*- coding: utf-8 -*-

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from landing.models import Callmecontact
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404



@receiver(post_save, sender=Callmecontact)
def send_mail_on_callback(sender, instance, created, **kwargs):
    if created:
        # chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        # reflink = get_random_string(4, chars) + str(instance.id)
        # Profile.objects.create(user=instance,reflink=reflink)
        context = {
		    'contact_name': instance.contact_name,
		    'callme_number': instance.id,
		    'contact_phone': instance.contact_phone,
		}
        subject = 'Заказ звонка № call-%s' % instance.id
        html_message = render_to_string('includes/mail_callme_template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'info@likwid.club'
        to = 'callmeback@likwid.club'
        if subject and html_message and from_email:
            try:
                if send_mail(subject, html_message, from_email, [to]):
                   instance.is_emailed = True
                   instance.save()
            except BadHeaderError:

                print('Invalid header found in email %s' % instance.id)
                return HttpResponse('Invalid header found %s' % instance.id)

            # education_order.is_emailed = True
            return HttpResponse('sended')
        else:
	        print('Make sure all fields are entered and valid %s' % instance.id)
	        # to get proper validation errors.
			# print('wring_any_field')
	        return HttpResponse('Make sure all fields are entered and valid %s' % instance.id)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
