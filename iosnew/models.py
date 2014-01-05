#coding:utf-8

from django.db import models

class TextInfo(models.Model):
    text       = models.TextField()
    url        = models.CharField(max_length=1024,blank=True)
    tagname    = models.CharField(max_length=64)


class ImgInfo(models.Model):
    image      = models.ImageField(upload_to='./image')
    url        = models.CharField(max_length=1024,blank=True)
    tagname    = models.CharField(max_length=64)

