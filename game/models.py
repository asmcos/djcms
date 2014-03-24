#coding:utf-8

from django.db import models



class TextInfo(models.Model):
    text       = models.TextField()
    tagname    = models.CharField(max_length=64)


class ImgInfo(models.Model):
    image      = models.ImageField(upload_to='./image')
    tagname    = models.CharField(max_length=64)
    def image_tag(self):
    	return u'<img src="/%s" />' % self.image
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class StudentsApp(models.Model):
    title1         = models.CharField(max_length=1024)
    title2         = models.CharField(max_length=1024)
    content        = models.TextField()
    imagemini      = models.ImageField(upload_to='./image',default='studentmini.png')
    imagebig       = models.ImageField(upload_to='./image',default='studentbig.png')
    order          = models.IntegerField(default=0)
    kw            = models.CharField(max_length=64,default='open')

class Teacher(models.Model):
    name        = models.CharField(max_length=64)
    content     = models.TextField()
    photo       = models.ImageField(upload_to='./image',default='teacher.png')
    background  = models.ImageField(upload_to='./image',default='teacherbg.png')
    order       = models.IntegerField(default=0)
    kw            = models.CharField(max_length=64,default='open')
class Singlepage(models.Model):
    title         = models.CharField(max_length=1024)
    content       = models.TextField()
    image         = models.ImageField(upload_to='./image',default='page.png')
    order         = models.IntegerField(default=0)
    count         = models.IntegerField(default=0)
    kw            = models.CharField(max_length=64,default='open')
