# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=8, verbose_name='CEP')),
                ('action_flag', models.CharField(choices=[('1', 'Added'), ('2', 'Deleted'), ('3', 'Detailed')], max_length=1, verbose_name='Action Flag')),
                ('action_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]