# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_image', '0002_auto_20170621_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='Imagesss'),
        ),
    ]
