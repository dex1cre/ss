# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_image', '0007_auto_20170622_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='Изображение'),
        ),
    ]
