# coding:utf-8
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context
from django.template import RequestContext
import os, datetime
from .models import *


def make_model_count(model,count,part=None):
	name = model._meta.object_name.lower()
	db   = model.objects.all()[:count]
	d = {}

	d[name+"count"] = len(db)

 
	if part != None:
		l = (count + part) / part 	
		for i in range(0,l):
			d["object_"+name + str(i)] = db[i * part:i * part +part]
	else:
		d["object_"+name] = db
	return d

def mainpage(request):  # mainpage
    alltext = TextInfo.objects.all()
    allimg = ImgInfo.objects.all()
    d = {}
    for text in alltext:
	d[text.tagname]        = text.text
    for img in allimg:
	d[img.tagname]        = img.image

    d1 = make_model_count(StudentsApp,6,3) 
    d.update(d1)

    return render_to_response('mainpage_tag.html',d,context_instance=RequestContext(request))

def mainpageenglish(request):  # mainpageenglish
    return render_to_response('mainpageenglish.html', context_instance=RequestContext(request))

def simple(request):  # simple中文页面
    return render_to_response('simple.html', context_instance=RequestContext(request))

def simpleenglish(request):  # simple
    return render_to_response('simpleenglish.html', context_instance=RequestContext(request))
