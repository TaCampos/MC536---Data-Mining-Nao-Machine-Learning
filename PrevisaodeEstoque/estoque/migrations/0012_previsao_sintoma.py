# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0011_auto_20161125_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='previsao',
            name='sintoma',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estoque.Sintoma'),
        ),
    ]
