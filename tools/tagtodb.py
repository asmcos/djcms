import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iosnew.settings")
sys.path.append('./')
import iosnew.settings        

from iosnew.models import TextInfo,ImgInfo

import re
import sys

input_file = sys.argv[1]

buf = open(input_file).read()

all_text_tag = re.findall('\{\{(tag\d+?)\|default:"(.*?)"\}\}',buf,re.S)
print "Text have %d" % len(all_text_tag)

for a in all_text_tag:
	try:
		a1 = TextInfo.objects.get(tagname=a[0])
		#a1.text = a[1]
		#a1.save()
	except:
		a1 = TextInfo(text=a[1],tagname=a[0])
		a1.save()



all_img_tag = re.findall("\{\{(tagimg\d+?)\|default:'(.*?)'\}\}",buf,re.S)
print "Image have %d" % len(all_img_tag)

for a in all_img_tag:
	try:
		a1 = ImgInfo.objects.get(tagname=a[0])
		#a1.image = a[1]
		#a1.save()
	except:
		a1 = ImgInfo(image=a[1],tagname=a[0])
		a1.save()
