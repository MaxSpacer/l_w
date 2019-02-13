# -*- coding: utf-8 -*-

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import EventJoiner
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404


@receiver(post_save, sender=EventJoiner)
def send_mail_join_event(sender, instance, created, **kwargs):
    if created:
        context = {
		    'order_name': instance.customer_name,
		    'order_number': instance.pk,
		    'order_eve': instance.event,
		    'contact_phone': instance.customer_phone,
		    'contact_email': instance.customer_email,
		}
        subject = 'Запись на мероприятие № EVE-%s' % instance.pk
        html_message = render_to_string('mail_templates/mail_template_event_join.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'info@likwid.club'
        to = 'join_event@likwid.club'
        if instance.is_emailed == False:
            if subject and html_message and from_email:
                try:
                    if send_mail(subject, plain_message, from_email, [to]):
                        EventJoiner.objects.filter(pk=instance.pk).update(is_emailed=True)
                        instance.is_emailed = True
                except BadHeaderError:
                    return print('Invalid header found in email %s' % instance.pk)
                return print('email is sended %s' % instance.pk)
            else:
    	        return print('Make sure all fields are entered and valid %s' % instance.pk)
