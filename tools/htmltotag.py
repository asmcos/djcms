#coding:utf-8
import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

buf = open(input_file).read()


# get exist tag count.
all_tag = re.findall("\{\{tag(.*?)\|default:.*?\}\}",buf,re.S)
count = len(all_tag) + 1
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

