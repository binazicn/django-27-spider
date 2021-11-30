# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class spiderdb(models.Model):
    url = models.URLField('URL地址',max_length=100 )
    jpg = models.CharField('jpg地址',max_length=1000)
    m3u8 = models.CharField('m3u8地址',max_length=100)
    gif = models.CharField('gif地址',max_length=1000)
    dir_url = models.CharField('文件夹名称',max_length=50)
    crawled = models.CharField('创建时间',max_length=40)
    spider = models.CharField('项目名称',max_length=50)