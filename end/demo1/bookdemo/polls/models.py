from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """
    自定义用户类继承django自带用户系统
    """
    telephone = models.CharField(max_length=11, verbose_name="手机号")
    pollss = models.ManyToManyField('Polls')


class Polls(models.Model):
    # 问题类
    polls_text = models.CharField(max_length=20)

    def __str__(self):
        return self.polls_text


class Pollsmsg(models.Model):
    # 选项类
    msg = models.CharField(max_length=20, verbose_name="内容")
    coutmsg = models.PositiveIntegerField(verbose_name="数量", default=0)

    polls = models.ForeignKey(Polls, on_delete=models.CASCADE)

    def __str__(self):
        return self.msg
