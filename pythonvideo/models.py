#coding=utf-8
from django.db import models


class Category(models.Model):
	image	   = models.ImageField(upload_to='./image')
	icon	   = models.CharField(max_length=64)
	count      = models.IntegerField(default=0)
	title      = models.CharField(max_length=256)
	intro      = models.CharField(max_length=1024)
	order      = models.IntegerField(default=0)
	kw	   = models.CharField(max_length=64,default="")
	createdate = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.title
class Course(models.Model):
	title      = models.CharField( max_length=256)
	count      = models.IntegerField(default=0)
	intro      = models.CharField( max_length=1024)
	image	   = models.ImageField(upload_to='./image')
	cateid     = models.ForeignKey(Category)
	createdate = models.DateField(auto_now=True)
	order      = models.IntegerField(default=0)
	kw	   = models.CharField(max_length=64,default="")
	def __unicode__(self):
		return self.title

class Video(models.Model):
	title      = models.CharField( max_length=256)
	url	   = models.CharField( max_length=4096)
	count      = models.IntegerField(default=0)
	content    = models.TextField()
	intro      = models.CharField( max_length=1024)
	image	   = models.ImageField(upload_to='./image')
	courseid   = models.ForeignKey(Course)
	createdate = models.DateField(auto_now=True)
	order      = models.IntegerField(default=0)
	kw	   = models.CharField(max_length=64,default="")



class TextInfo(models.Model):
    text       = models.TextField()
    tagname    = models.CharField(max_length=64)


class ImgInfo(models.Model):
    image      = models.ImageField(upload_to='./image')
    tagname    = models.CharField(max_length=64)

