# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.TextField()),
                ('cost', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField()),
                ('complete', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('complete', models.BooleanField()),
                ('successful', models.BooleanField()),
                ('service_provider', models.OneToOneField(to='app.ServiceProvider')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.OneToOneField(to='app.UserProfile'),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='user',
            field=models.OneToOneField(to='app.UserProfile'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(to='app.UserProfile'),
        ),
    ]
