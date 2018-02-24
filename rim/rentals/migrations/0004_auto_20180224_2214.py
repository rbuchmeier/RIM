# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-24 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0003_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='gear',
        ),
        migrations.AddField(
            model_name='gear',
            name='rental',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rentals.Rental'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rental',
            name='rental_date',
            field=models.DateField(verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(verbose_name='end date'),
        ),
    ]
