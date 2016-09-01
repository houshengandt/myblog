# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markdownx.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length=30)),
                ('body', markdownx.models.MarkdownxField(verbose_name='正文')),
                ('pub_time', models.DateTimeField(verbose_name='发布时间', default=django.utils.timezone.now)),
                ('abstract', models.TextField(verbose_name='摘要')),
                ('view_times', models.IntegerField(verbose_name='浏览数', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('comments', models.TextField(verbose_name='评论')),
                ('comment_pub_time', models.DateTimeField(verbose_name='评论发布时间', default=django.utils.timezone.now)),
                ('comment_by', models.CharField(verbose_name='评论者', max_length=30)),
                ('article', models.ForeignKey(related_name='comment', to='blog.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(verbose_name='标签', max_length=20)),
                ('article', models.ManyToManyField(related_name='tags', to='blog.Article')),
            ],
        ),
    ]
