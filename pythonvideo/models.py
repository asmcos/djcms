#coding=utf-8
from django.db import models


class Category(models.Model):
	image	   = models.ImageField(upload_to='./image',default="./image/defaultcate.jpg")
	icon	   = models.CharField(max_length=64)
	count      = models.IntegerField(default=0)
	title      = models.CharField(max_length=256)
	intro      = models.CharField(max_length=1024,default='分类')
	order      = models.IntegerField(default=0)
	kw	   = models.CharField(max_length=64,default="open")
	createdate = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.title
class Course(models.Model):
	title      = models.CharField( max_length=256)
	count      = models.IntegerField(default=0)
	intro      = models.CharField( max_length=1024,default='课程')
	image	   = models.ImageField(upload_to='./image',default="./image/defaultcourse.jpg")
	cateid     = models.ForeignKey(Category)
	createdate = models.DateField(auto_now=True)
	order      = models.IntegerField(default=0)
	kw	   = models.CharField(max_length=64,default="open")
	def __unicode__(self):
		return self.title

class Video(models.Model):
	title      = models.CharField( max_length=256)
	url	   = models.CharField( max_length=4096)
	count      = models.IntegerField(default=0)
	content    = models.TextField(default="视频")
	intro      = models.CharField( max_length=1024)
	image	   = models.ImageField(upload_to='./image',default="./image/defaultvideo.jpg")
	courseid   = models.ForeignKey(Course)
	createdate = models.DateField(auto_now=True)
	order      = models.IntegerField(default=0)
	kw	   = models.CharField(max_length=64,default="open")



class TextInfo(models.Model):
    text       = models.TextField()
    tagname    = models.CharField(max_length=64)


class ImgInfo(models.Model):
    image      = models.ImageField(upload_to='./image')
    tagname    = models.CharField(max_length=64)

