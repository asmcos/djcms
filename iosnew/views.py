# coding:utf-8
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context
from django.template import RequestContext
import os, datetime

def mainpage(request):  # mainpage
    return render_to_response('mainpage.html', context_instance=RequestContext(request))

def mainpageenglish(request):  # mainpageenglish
    return render_to_response('mainpageenglish.html', context_instance=RequestContext(request))

def simple(request):  # simple中文页面
    return render_to_response('simple.html', context_instance=RequestContext(request))

def simpleenglish(request):  # simple
    return render_to_response('simpleenglish.html', context_instance=RequestContext(request))
