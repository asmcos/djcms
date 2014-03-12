#coding:utf-8

from django.template import Template,Context
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *

def home(request):
	d	= {}
	cates	= Category.objects.all().order_by('-id')[:4]
	courses	= Course.objects.all().order_by('-id')[:4]
	videos	= Video.objects.all().order_by('-id')[:4]
	d['cates']=cates
	d['courses']=courses
	d['videos']=videos
        alltext = TextInfo.objects.all()
        allimg = ImgInfo.objects.all()
        for text in alltext:
		d[text.tagname]        = text.text
        for img in allimg:
		d[img.tagname]        = img.image


	return render_to_response('pythonvideo/home_tag.html',d,context_instance=RequestContext(request))
def cates(request):
	d	= {}
	cates	= Category.objects.all().order_by('-id')
	
	d['cates']=cates
 	alltext = TextInfo.objects.all()
        allimg = ImgInfo.objects.all()
        for text in alltext:
		d[text.tagname]        = text.text
        for img in allimg:
		d[img.tagname]        = img.image
	
	return render_to_response('pythonvideo/cates.html',d,context_instance=RequestContext(request))
				
def courses(request):
	d	= {}
	if 'cateid' in request.GET:
		courses = Course.objects.filter(cateid=request.GET['cateid']).order_by('-id')
	else:
		courses	= Course.objects.all().order_by('-id')
	
	d['courses']=courses
 	alltext = TextInfo.objects.all()
        allimg = ImgInfo.objects.all()
        for text in alltext:
		d[text.tagname]        = text.text
        for img in allimg:
		d[img.tagname]        = img.image
	
	return render_to_response('pythonvideo/courses_tag.html',d,context_instance=RequestContext(request))
def videos(request):
	d	= {}
	p = 0
	if 'page' in request.GET:
		p = int(request.GET['page'])-1
	if 'vid' in request.GET:
		videos	= Video.objects.filter(cateid=request.GET['vid']).order_by('-id')
	else:
		videos  = Video.objects.all().order_by('id')
	print len(videos)
	videos = list(videos)[p * 9: (p+1) * 9]

	d['videos']=videos
	print len(videos)
	d['page_next'] = p+2
	return render_to_response('pythonvideo/videos_tag.html',d,context_instance=RequestContext(request))

def video(request,id):
	d	= {}

	videos	= Video.objects.filter(courseid=id)
	
	d['videos']	=videos
		

	d['courses']	= Course.objects.get(id=id)
	if 'vid' in request.GET:
		d['vid'] = Video.objects.get(id=request.GET['vid'])
		d['vid'].count+=1
		d['vid'].save()
	else:
		if videos:
			d['vid'] = list(videos)[0]
 	alltext = TextInfo.objects.all()
        allimg = ImgInfo.objects.all()
        for text in alltext:
		d[text.tagname]        = text.text
        for img in allimg:
		d[img.tagname]        = img.image
	
	return render_to_response('pythonvideo/video_tag.html',d,context_instance=RequestContext(request))
				
			
