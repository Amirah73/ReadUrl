
#read Url 


import urllib.request
import urllib.parse
page=urllib.request.urlopen("https://simple.wikipedia.org/wiki/Jeddah")
for line in page:
   decoded_line = line.decode("utf-8")
   print(decoded_line)
