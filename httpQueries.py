#
# Query google for something. Just an exercise.
#

import urllib2
import urllib
import json

url = "https://www.google.com/search#"
hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

query = raw_input("What do you want to search for ? >> ")
query = urllib.urlencode( {'q' : query } )

print("Querying: "+url+query)

req = urllib2.Request(url, headers=hdr)

try:
    page = urllib2.urlopen (url + query)
except urllib2.HTTPError, e:
    print "error!!!!!!"
    print e.fp.read()

content = page.read()
print content
