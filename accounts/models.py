from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reflink = models.CharField("www.likwid.club/ref/", max_length=16, blank=False)
    referals_qty = models.IntegerField("Кол-во рефералов", default=0)

    def __str__(self):
        return "%s" % self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        reflink = get_random_string(4, chars) + str(instance.id)
        Profile.objects.create(user=instance,reflink=reflink)

# @receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
