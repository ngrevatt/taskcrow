# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161016_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$20000$WnhvNVLfaG86$Rn0zycYpO4sK2p9RfyxvJ3Q10VF5+6qcUxzjC7JFR2I=', max_length=128),
            preserve_default=False,
        ),
    ]
