# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-09 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0016_auto_20180409_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalGear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='packagerental',
            name='package',
        ),
        migrations.RemoveField(
            model_name='packagerental',
            name='rental',
        ),
        migrations.RemoveField(
            model_name='gear',
            name='package_rental',
        ),
        migrations.AddField(
            model_name='rental',
            name='package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rentals.PackageValue'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PackageRental',
        ),
        migrations.AddField(
            model_name='rentalgear',
            name='gear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.Gear'),
        ),
        migrations.AddField(
            model_name='rentalgear',
            name='rental',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.Rental'),
        ),
    ]
