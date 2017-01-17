from django.db import models


class BaiduUser(models.Model):
    username = models.CharField("baidu用户名", max_length=50, unique=True)
    password = models.CharField("baidu密码", max_length=50)
    check_in_times = models.IntegerField("签到次数", default=0)
    wealth = models.IntegerField("财富值", default=0)
    ticket = models.IntegerField("下载券", default=0)
    last_checkin_time = models.TimeField("上次签到时间", auto_now=True)
