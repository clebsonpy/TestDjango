# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artigo',
            options={'ordering': ('-publicacao',)},
        ),
        migrations.AlterField(
            model_name='artigo',
            name='publicacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]