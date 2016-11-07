# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 06:53
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='The actual question itself.', verbose_name='question')),
                ('answer', models.TextField(blank=True, help_text='The answer text.', verbose_name='answer')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive'), (2, 'Group Header')], default=0, help_text="Only questions with their status set to 'Active' will be displayed. Questions marked as 'Group Header' are treated as such by views and templates that are set up to use them.", verbose_name='status')),
                ('protected', models.BooleanField(default=False, help_text='Set true if this question is only visible by authenticated users.', verbose_name='is protected')),
                ('sort_order', models.IntegerField(default=0, help_text='The order you would like the question to be displayed.', verbose_name='sort order')),
                ('created_on', models.DateTimeField(default=datetime.datetime.now, verbose_name='created on')),
                ('updated_on', models.DateTimeField(verbose_name='updated on')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
            ],
            options={
                'ordering': ['sort_order', 'created_on'],
                'verbose_name': 'Frequent asked question',
                'verbose_name_plural': 'Frequently asked questions',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('slug', models.SlugField(max_length=150, verbose_name='slug')),
                ('sort_order', models.IntegerField(default=0, help_text='The order you would like the topic to be displayed.', verbose_name='sort order')),
            ],
            options={
                'ordering': ['sort_order', 'name'],
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='faq.Topic', verbose_name='topic'),
        ),
        migrations.AddField(
            model_name='question',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='updated by'),
        ),
    ]
