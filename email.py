import re,urllib2
emailsearch=re.compile(r'[\w*\.]+@[\w*\.]+')
files=urllib2.urlopen("web link")
code=files.read()
m=emailsearch.findall(code)
fopen=open('file name ','w')
for i in m:
    fopen.write(i+'\n')
fopen.close()
