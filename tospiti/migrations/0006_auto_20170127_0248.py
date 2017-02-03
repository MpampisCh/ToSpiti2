# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 00:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tospiti', '0005_auto_20170127_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='prop_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='tospiti.Prop_Category', verbose_name='Είδος κατοικίας'),
        ),
    ]