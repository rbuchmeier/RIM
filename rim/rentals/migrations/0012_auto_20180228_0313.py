# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-28 03:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0011_auto_20180228_0252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gear',
            old_name='rental',
            new_name='package_rental',
        ),
    ]