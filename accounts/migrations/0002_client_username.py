# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(default='test', max_length=30, verbose_name=b'username'),
            preserve_default=False,
        ),
    ]
