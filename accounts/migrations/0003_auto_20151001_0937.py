# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_client_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(unique=True, max_length=30, verbose_name=b'username'),
        ),
    ]
