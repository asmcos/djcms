# coding:utf-8
from django.shortcuts import render_to_response
from iosnew.models import *


def home(request):  # mainpage
    alltext = TextInfo.objects.all()
    allimg = ImgInfo.objects.all()
    d = {}
    for text in alltext:
	d[text.tagname]        = text.text
    for img in allimg:
	d[img.tagname]        = img.image


    return render_to_response('jeap_main_tag.html',d)

