# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-14 13:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_member_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=255)),
                ('release_date', models.DateField(default=datetime.date.today)),
                ('number_of_page', models.IntegerField(default=0)),
                ('langage', models.CharField(max_length=255)),
                ('isnb', models.CharField(max_length=255)),
                ('image', models.ImageField(default='../users.png', upload_to='')),
                ('category', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='api.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renting_date', models.DateField(default=datetime.date.today)),
                ('returning_date', models.DateField(default=datetime.date.today)),
                ('status', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent', to='api.Book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent', to='api.Member')),
            ],
        ),
    ]
