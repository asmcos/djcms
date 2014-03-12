#coding:utf-8
import sys
import re

buf = open(sys.argv[1]).read()
buf1  = buf.replace(r"file:///D|/MyBackup/我的文档/Downloads/","")
open(sys.argv[2],"w+").write(buf1)
