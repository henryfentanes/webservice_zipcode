from __future__ import unicode_literals

from django.db import models


class Zipcode(models.Model):
    zip_code = models.CharField('CEP', max_length=8, primary_key=True)
    address = models.CharField(
        'Logradouro', max_length=100, blank=True, null=True)
    neighborhood = models.CharField(
        'Bairro', max_length=50, blank=True, null=True)
    state = models.CharField('Estado', max_length=2, blank=True, null=True)
    city = models.CharField('Cidade', max_length=50, blank=True, null=True)
