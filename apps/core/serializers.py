# coding: utf-8
from __future__ import absolute_import
from apps.core.models import Zipcode
from rest_framework import serializers


class ZipcodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zipcode
        fields = ('zip_code', 'address', 'neighborhood', 'state', 'city')
