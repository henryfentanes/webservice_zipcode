# coding: utf-8
from __future__ import absolute_import
from django.views.generic import TemplateView
from apps.core.models import Zipcode

from rest_framework import viewsets
from apps.core.serializers import ZipcodeSerializer


class Home(TemplateView):
    template_name = 'core/index.html'


class ZipcodeViewSet(viewsets.ModelViewSet):
    queryset = Zipcode.objects.all()
    serializer_class = ZipcodeSerializer
