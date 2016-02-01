# coding: utf-8
from __future__ import absolute_import
from apps.core.models import Zipcode, LogAction
from rest_framework import serializers


class ZipcodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zipcode
        fields = ('zip_code', 'address', 'neighborhood', 'state', 'city')


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LogAction
        fields = ('zip_code', 'get_action_flag_display', 'action_time_display')
