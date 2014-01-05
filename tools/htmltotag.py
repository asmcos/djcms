#coding:utf-8
import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

buf = open(input_file).read()


all_src_tag = re.findall("\{\[(.*?)\]\}",buf,re.S)
print all_src_tag
buf1 = buf
count = 1
for a in all_src_tag:
	a1 = '{{tag' +str(count) +"|default:'" + a +"'}}" 	
	buf1 = buf1.replace("{["+a+"]}",a1,1)
	count += 1
open(output_file,"w").write(buf1)

