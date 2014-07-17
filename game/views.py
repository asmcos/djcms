# coding:utf-8
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import os, datetime
from .models import *


def make_model_count(model,count,part=None):
	name = model._meta.object_name.lower()
	db   = model.objects.all().order_by('-id')[:count]
	d = {}

	d[name+"count"] = len(db)

 
	if part != None:
		l = (count + part) / part 	
		for i in range(0,l):
			d["object_"+name + str(i)] = db[i * part:i * part +part]
	else:
		d["object_"+name] = db
	return d

def home(request):  # mainpage
    d = {}
    alltext = TextInfo.objects.all()
    allimg = ImgInfo.objects.all()
    for text in alltext:
	d[text.tagname]        = text.text
    for img in allimg:
	d[img.tagname]        = str(img.image)


    course5 = Singlepage.objects.filter(order__gte = 10000).order_by('order')[0:5]	
    d['course5']=course5

    '''
    d1 = make_model_count(StudentsApp,6,3) 
    d.update(d1)

    d1 = make_model_count(Teacher,3)
    d.update(d1)
    '''
    return render_to_response('game/game_main_tag.html',d,context_instance=RequestContext(request))


def listpage(request):  
    d = {}
    alltext = TextInfo.objects.all()
    allimg = ImgInfo.objects.all()
    for text in alltext:
        d[text.tagname]        = text.text
    for img in allimg:
	d[img.tagname]        =  "/"+str(img.image)

    d['projects'] = StudentsApp.objects.all()

    return render_to_response('game/game_lists.html',d,context_instance=RequestContext(request))

def teachers(request):
    d = {}
    alltext = TextInfo.objects.all()
    allimg = ImgInfo.objects.all()
    for text in alltext:
        d[text.tagname]        = text.text
    for img in allimg:
	d[img.tagname]        =  "/"+str(img.image)


    d['teachers'] = Teacher.objects.all().order_by('-order')

    return render_to_response('game/game_teacher.html',d,context_instance=RequestContext(request))

def aboutus(request):
    d = {}
    alltext = TextInfo.objects.all()
    allimg = ImgInfo.objects.all()
    for text in alltext:
        d[text.tagname]        = text.text
    for img in allimg:
	d[img.tagname]        =  img.image


    return render_to_response('game/aboutus_tag.html',d,context_instance=RequestContext(request))




def showpage(request,id):
    d = {}
    alltext = TextInfo.objects.all()
    allimg  = ImgInfo.objects.all()

    for text in alltext:
        d[text.tagname]       = text.text
    for img in allimg:
	d[img.tagname]        = "/"+str(img.image)

 
    start = int(id)-2
    if start < 0:
	start = 0
    d['pages'] = Singlepage.objects.filter()[start:int(id)+2]
    try:
    	d['page'] = Singlepage.objects.get(id=id)
	d['page'].count += 1
    except:
	d['page'] = 'Page Not Found'

    return render_to_response('game/show-single.html',d,context_instance=RequestContext(request))


