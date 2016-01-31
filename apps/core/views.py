# coding: utf-8
from __future__ import absolute_import
import requests
import json
from django.http import Http404
from django.views.generic import TemplateView
from apps.core.models import Zipcode

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.core.serializers import ZipcodeSerializer


class Home(TemplateView):
    template_name = 'core/index.html'


class ZipcodeViewSet(viewsets.ModelViewSet):
    queryset = Zipcode.objects.all()
    serializer_class = ZipcodeSerializer

    def create(self, request, *args, **kwargs):
        postmon = requests.get(
            'http://api.postmon.com.br/v1/cep/%s' % (request.data['zip_code']))
        if postmon.status_code == 200:
            postmon_data = json.loads(postmon.content)
            cleaned_data = self.clean_zipcode(postmon_data)
        else:
            raise Http404('Não foi possível encontrar dados do cep no Postmon')

        serializer = self.get_serializer(data=cleaned_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def clean_zipcode(self, data):
        cleaned_data = {}
        for field in Zipcode._meta.fields:
            if field.verbose_name.lower() in data:
                cleaned_data[field.name] = data[field.verbose_name.lower()]
            else:
                cleaned_data[field.name] = ''
        return cleaned_data
