# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0005_remove_medicamento_laboratorio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refere',
            name='sintoma',
        ),
        migrations.RemoveField(
            model_name='refere',
            name='termo',
        ),
        migrations.RemoveField(
            model_name='busca',
            name='termo',
        ),
        migrations.AddField(
            model_name='busca',
            name='sintoma',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estoque.Sintoma'),
        ),
        migrations.DeleteModel(
            name='Refere',
        ),
        migrations.DeleteModel(
            name='Termo',
        ),
    ]
