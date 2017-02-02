from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tag = models.CharField('标签', max_length=10)


class TodoList(models.Model):
    user = models.ForeignKey(User, related_name='tasks')
    task = models.CharField('任务', max_length=50)
    remark = models.TextField('备注', max_length=500, null=True)
    state = models.BooleanField('状态', default=False)
    created_time = models.DateTimeField('创建日期', auto_now_add=True)
    changed_time = models.DateTimeField('修改日期', auto_now=True)
    completed_time = models.DateTimeField('完成日期', null=True)
    tag = models.ForeignKey(Tag, null=True, related_name='to_do_list_tag')
