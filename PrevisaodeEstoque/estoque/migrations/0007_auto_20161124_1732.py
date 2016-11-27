# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0006_auto_20161118_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Previsao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
                ('resultado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Relaciona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previsao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Previsao')),
                ('sintoma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Sintoma')),
            ],
        ),
        migrations.RemoveField(
            model_name='trata',
            name='doenca',
        ),
        migrations.RemoveField(
            model_name='trata',
            name='dosagem',
        ),
        migrations.AddField(
            model_name='trata',
            name='sintoma',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estoque.Sintoma'),
        ),
    ]
