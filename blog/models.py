from django.db import models
from django.utils import timezone

from markdownx.models import MarkdownxField


class Article(models.Model):
    title = models.CharField("标题", max_length=30)
    body = MarkdownxField("正文")
    pub_time = models.DateTimeField("发布时间", default=timezone.now)
    abstract = models.TextField("摘要")
    view_times = models.IntegerField("浏览数", default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/' + str(self.pub_time.date().year) + '/' + str(self.pub_time.date().month) + '/' + \
               str(self.pub_time.date().day) + '/' + str(self.pk)
        # todo 用reverse重写


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comment')
    comments = models.TextField("评论")
    comment_pub_time = models.DateTimeField("评论发布时间", default=timezone.now)
    comment_by = models.CharField("评论者", max_length=30)


class Tags(models.Model):
    article = models.ManyToManyField(Article, related_name='tags')
    tag_name = models.CharField("标签", max_length=20)
