#coding:utf-8

from django.template import Template,Context
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from .models import *
from game.models import *
from django.contrib.auth.decorators import user_passes_test
from django.forms import ModelForm

class UserForm(ModelForm):
     class Meta:
         model = UserJoin


def eventjoin(request,id):
	d	= {}
	try :
		event = Events.objects.get(id=int(id))
 		alltext = TextInfo.objects.all()
        	allimg = ImgInfo.objects.all()
        	for text in alltext:
			d[text.tagname]        = text.text
        	for img in allimg:
			d[img.tagname]        = img.image
		d['event'] = event
		return render_to_response('apply/join.html',d,context_instance=RequestContext(request))
	except:
		return redirect("/") 

def joinsave(request,id):
	d	= {}
	try :
		event = Events.objects.get(id=int(id))
 		alltext = TextInfo.objects.all()
        	allimg = ImgInfo.objects.all()
        	for text in alltext:
			d[text.tagname]        = text.text
        	for img in allimg:
			d[img.tagname]        = img.image
		d['event'] = event
		post = request.POST.copy()
		post['eventid'] = event.id
		post['kw'] = '0'
		form = UserForm(post)
		if form.is_valid():
			form.save()
		else:
			d['form'] = form
		return render_to_response('apply/joinok.html',d,context_instance=RequestContext(request))
	except:
		d['form'] = "报名的活动不存在"
		return render_to_response('apply/joinok.html',d,context_instance=RequestContext(request))

	

@user_passes_test(lambda u: u.is_staff)	
def eventadmin(request,id):
		d	= {}
	#try :
		event    = Events.objects.get(id=int(id))
 		alltext  = TextInfo.objects.all()
        	allimg   = ImgInfo.objects.all()
		allusers = UserJoin.objects.filter(eventid = event) 
        	for text in alltext:
			d[text.tagname]        = text.text
        	for img in allimg:
			d[img.tagname]        = img.image
		d['event']    = event
		d['allusers'] = allusers
		print allusers
		return render_to_response('apply/userlist.html',d,context_instance=RequestContext(request))
	#except:
		return redirect("/") 


def listuser(request,id):
        d       = {}
        try :
                event    = Events.objects.get(id=int(id))
                allusers = UserJoin.objects.filter(eventid = event).filter(kw="1")
                d['event']    = event
                d['allusers'] = allusers
                return render_to_response('apply/confirmlist.html',d,context_instance=RequestContext(request))
        except:
                return redirect("/") 


@user_passes_test(lambda u: u.is_staff)	
def confirm(request,eventid,id):
        try :
                user     = UserJoin.objects.get(id=int(id))
		if user.kw == "0":
			user.kw = "1"
		else:	
			user.kw = "0"
		user.save()
	except:
		pass	
        return redirect("/apply/eventadmin/%s"%eventid)

@user_passes_test(lambda u: u.is_staff)	
def delete(request,eventid,id):
        try :
                user     = UserJoin.objects.get(id=int(id))
		user.delete()
	except:
		pass
        return redirect("/apply/eventadmin/%s"%eventid)
	
