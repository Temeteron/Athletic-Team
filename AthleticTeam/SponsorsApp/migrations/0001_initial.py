# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='photos/index.png', upload_to='photos/')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('info', models.TextField(blank=True)),
            ],
        ),
    ]