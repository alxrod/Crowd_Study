# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-11 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qText', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Sgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='sgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Sgroup'),
        ),
    ]
