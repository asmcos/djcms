#coding:utf-8

from django.db import models

class TextInfo(models.Model):
    text       = models.TextField()
    tagname    = models.CharField(max_length=64)


class ImgInfo(models.Model):
    image      = models.ImageField(upload_to='./image')
    tagname    = models.CharField(max_length=64)

class StudentsApp(models.Model):
    title1         = models.CharField(max_length=1024)
    title2         = models.CharField(max_length=1024)
    content        = models.TextField()
    imagemini      = models.ImageField(upload_to='./image')
    imagebig       = models.ImageField(upload_to='./image')
    url            = models.CharField(max_length=1024)

class Teacher(models.Model):
    name        = models.CharField(max_length=64)
    intro       = models.CharField(max_length=1024)
    photo       = models.ImageField(upload_to='./image')
 
