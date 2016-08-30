# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('body', models.TextField(verbose_name='正文')),
                ('pub_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('abstract', models.TextField(verbose_name='摘要')),
                ('view_times', models.IntegerField(default=0, verbose_name='浏览数')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('comments', models.TextField(verbose_name='评论')),
                ('comment_pub_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='评论发布时间')),
                ('comment_by', models.CharField(max_length=30, verbose_name='评论者')),
                ('article', models.ForeignKey(related_name='comment', to='blog.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tag_name', models.CharField(max_length=20, verbose_name='标签')),
                ('article', models.ManyToManyField(related_name='tags', to='blog.Article')),
            ],
        ),
    ]
