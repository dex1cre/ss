# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_image', '0005_auto_20170622_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagetag',
            old_name='author',
            new_name='image',
        ),
    ]