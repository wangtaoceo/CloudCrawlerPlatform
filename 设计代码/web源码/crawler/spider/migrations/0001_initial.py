# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crawler',
            fields=[
                ('crawler_id', models.AutoField(primary_key=True, serialize=False)),
                ('crawler_name', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('remark', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='mycrawler',
            fields=[
                ('crawler_id', models.AutoField(primary_key=True, serialize=False)),
                ('crawler_name', models.CharField(max_length=20)),
                ('spiderfile', models.CharField(max_length=50)),
                ('remark', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('crawler_num', models.IntegerField(default=0)),
                ('crawler_num_now', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='crawler',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crawler_set', to='spider.User'),
        ),
    ]
