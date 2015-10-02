# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name=b'last name', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'email address', db_index=True)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('email_confirm_key', models.CharField(max_length=32, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.date(2015, 10, 1))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SendSMS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to_number', models.CharField(max_length=30)),
                ('from_number', models.CharField(max_length=30)),
                ('sms_sid', models.CharField(default=b'', max_length=34, blank=True)),
                ('account_sid', models.CharField(default=b'', max_length=34, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sent_at', models.DateTimeField(null=True, blank=True)),
                ('delivered_at', models.DateTimeField(null=True, blank=True)),
                ('status', models.CharField(default=b'', max_length=20, blank=True)),
            ],
        ),
    ]
