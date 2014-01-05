import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iosnew.settings")
sys.path.append('./')
import iosnew.settings        

from iosnew.models import TextInfo,ImgInfo

alltext = TextInfo.objects.all()
aimg = ImgInfo.objects.all()

for a in aimg:
	print a.image


