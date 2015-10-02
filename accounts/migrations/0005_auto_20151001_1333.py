# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20151001_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email_confirm_key',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='key_expires',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
