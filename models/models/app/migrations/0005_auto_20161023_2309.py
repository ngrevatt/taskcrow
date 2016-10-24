# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_authenticationtoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AlterField(
            model_name='task',
            name='customer',
            field=models.ForeignKey(to='app.User'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
