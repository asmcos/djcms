#coding:utf-8
import re
import sys,os

input_file = sys.argv[1]
output_file = sys.argv[2]


dict_file = {'home.html':0,'cates.html':1000,'courses.html':2000,'base.html':3000,'video.html':4000,'videos.html':5000}

buf = open(input_file).read()


# get exist tag count.
all_tag = re.findall("\{\{tag(.*?)\|default:.*?\}\}",buf,re.S)
count = len(all_tag) + 1 + dict_file[os.path.basename(sys.argv[1])]
print count



all_text_tag = re.findall("\{\[(.*?)\]\}",buf,re.S)
buf1 = buf
for a in all_text_tag:
	a1 = '{{tag' +str(count) +'|default:"' + a +'"}}' 	
	buf1 = buf1.replace("{["+a+"]}",a1,1)
	count += 1



all_img_tag = re.findall("\[\{(.*?)\}\]",buf,re.S)
for a in all_img_tag:
	a1 = '{{tagimg' +str(count) +"|default:'" + a +"'}}" 	
	buf1 = buf1.replace("[{"+a+"}]",a1,1)
	count += 1

open(output_file,"w").write(buf1)
