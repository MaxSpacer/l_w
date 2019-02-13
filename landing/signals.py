# -*- coding: utf-8 -*-

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Callmecontact
from .models import Mainformcontact
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404



@receiver(post_save, sender=Callmecontact)
def send_mail_on_callback(sender, instance, created, **kwargs):
    if created:
        context = {
		    'contact_name': instance.contact_name,
		    'callme_number': instance.id,
		    'contact_phone': instance.contact_phone,
		}
        subject = 'Заказ звонка № call-%s' % instance.id
        html_message = render_to_string('mail_templates/mail_callme_template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'info@likwid.club'
        to = 'callmeback@likwid.club'
        print(instance.is_emailed)
        if instance.is_emailed == False:
            if subject and html_message and from_email:
                try:
                    if send_mail(subject, html_message, from_email, [to]):
                        Callmecontact.objects.filter(pk=instance.pk).update(is_emailed=True)
                        instance.is_emailed = True
                        # print(instance.is_emailed)

                except BadHeaderError:
                    print('Invalid header found in email %s' % instance.id)
                    return HttpResponse('Invalid header found %s' % instance.id)
                # education_order.is_emailed = True
                return HttpResponse('sended')
            else:
    	        print('Make sure all fields are entered and valid %s' % instance.id)

    	        return HttpResponse('Make sure all fields are entered and valid %s' % instance.id)

@receiver(post_save, sender=Mainformcontact)
def send_mail_main_form(sender, instance, created, **kwargs):
    if created:
        context = {
		    'contact_name': instance.contact_name,
		    'main_form_number': instance.id,
		    'contact_phone': instance.contact_phone,
		    'contact_email': instance.contact_email,
		}
        subject = 'Новый контакт с главной страницы № MAIN-%s' % instance.id
        html_message = render_to_string('mail_templates/mail_main_form.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'info@likwid.club'
        to = 'main_customer@likwid.club'
        print(instance.is_emailed)
        if instance.is_emailed == False:
            if subject and html_message and from_email:
                try:
                    if send_mail(subject, html_message, from_email, [to]):
                        Mainformcontact.objects.filter(pk=instance.pk).update(is_emailed=True)
                        instance.is_emailed = True
                        # print(instance.is_emailed)

                except BadHeaderError:
                    print('Invalid header found in email %s' % instance.id)
                    return HttpResponse('Invalid header found %s' % instance.id)
                # education_order.is_emailed = True
                return HttpResponse('sended')
            else:
    	        print('Make sure all fields are entered and valid %s' % instance.id)

    	        return HttpResponse('Make sure all fields are entered and valid %s' % instance.id)
