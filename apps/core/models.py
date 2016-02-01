from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# from apps.core.signals import log_create


class Zipcode(models.Model):
    zip_code = models.CharField('CEP', max_length=8, primary_key=True)
    address = models.CharField(
        'Logradouro', max_length=100, blank=True, null=True)
    neighborhood = models.CharField(
        'Bairro', max_length=50, blank=True, null=True)
    state = models.CharField('Estado', max_length=2, blank=True, null=True)
    city = models.CharField('Cidade', max_length=50, blank=True, null=True)


class LogAction(models.Model):
    FLAG_CHOICE = (('1', 'Added'), ('2', 'Deleted'), ('3', 'Detailed'))

    zip_code = models.CharField('CEP', max_length=8)
    action_flag = models.CharField(
        'Action Flag', max_length=1, choices=FLAG_CHOICE)
    action_time = models.DateTimeField(auto_now=True)


# Signals

@receiver(post_save, sender=Zipcode, weak=False)
def log_create(sender, instance, **kwargs):
    if kwargs.get('created'):
        LogAction.objects.create(
            zip_code=instance.pk,
            action_flag='1')


@receiver(post_delete, sender=Zipcode, weak=False)
def log_delete(sender, instance, **kwargs):
    LogAction.objects.create(
        zip_code=instance.pk,
        action_flag='2')
