# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 10:49
from __future__ import unicode_literals

from django.db import migrations
import simplemde.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='markdown',
            field=simplemde.fields.SimpleMDEField(blank=True, null=True),
        ),
    ]
