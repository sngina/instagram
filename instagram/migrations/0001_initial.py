# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-07-10 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_photo', models.ImageField(null=True, upload_to='image /')),
                ('image_name', models.CharField(max_length=30)),
                ('image_caption', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=30)),
            ],
        ),
    ]