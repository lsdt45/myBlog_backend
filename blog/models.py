from __future__ import unicode_literals
from django.db import models
import django.utils.timezone as timezone


class article(models.Model):
    objects = None
    id = models.IntegerField(primary_key=True, verbose_name="文章ID")
    title = models.CharField(max_length=50, verbose_name="文章名")
    Introduction = models.TextField(default='', verbose_name="简介")
    category = models.CharField(max_length=50, verbose_name="分类")
    label = models.CharField(max_length=50, verbose_name="标签")
    content = models.TextField(default='', verbose_name="内容")
    likeNum = models.IntegerField(default=0, verbose_name="点赞数")
    comment = models.TextField(default='', verbose_name="评论")
    commentNum = models.IntegerField(default=0, verbose_name="评论数")
    addDate = models.DateTimeField(default=timezone.now, verbose_name="保存日期")
    modifyDate = models.DateTimeField(auto_now=True, verbose_name="最后修改日期")
    readNum = models.IntegerField(default=0, verbose_name="阅读次数")
    coverPath = models.CharField(max_length=100, verbose_name="封面地址")


class userInfo(models.Model):
    object = None
    index = models.AutoField(primary_key=True, verbose_name="序号")
    ip = models.CharField(max_length=50, verbose_name="IP地址")
    ad_info = models.JSONField(verbose_name="地区信息")
    time = models.TimeField(auto_now=True, verbose_name="时间")
