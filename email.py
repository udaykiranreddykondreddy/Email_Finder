import re,urllib2
emailsearch=re.compile(r'[\w*\.]+@[\w*\.]+')
files=urllib2.urlopen("http://kluniversity.in/contact.aspx")
code=files.read()
m=emailsearch.findall(code)
fopen=open('emails.csv','w')
for i in m:
    fopen.write(i+'\n')
fopen.close()
