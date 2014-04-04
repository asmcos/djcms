#coding:utf-8

from django.db import models

class Events(models.Model):
	title     = models.CharField(max_length=1024)
	order     = models.IntegerField(default=0)
    	count     = models.IntegerField(default=0)
    	kw        = models.CharField(max_length=64,default='open')
	def __unicode__(self):
                return self.title


class UserJoin(models.Model):
    name         = models.CharField(max_length=64)
    workage      = models.CharField(max_length=16)
    email        = models.EmailField(max_length=256)
    qq           = models.CharField(max_length=64,blank=True,null=True)
    company      = models.CharField(max_length=256)
    interest     = models.CharField(max_length=64)
    kw           = models.CharField(max_length=64,blank=True)
    eventid     = models.ForeignKey(Events)
    dt           = models.DateTimeField(auto_now_add=True)
