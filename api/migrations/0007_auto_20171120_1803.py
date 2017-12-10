# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-20 11:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171115_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent', to=settings.AUTH_USER_MODEL),
        ),
    ]
