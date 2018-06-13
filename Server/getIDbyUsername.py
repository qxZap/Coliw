import urllib2
import sys

def getIDbyUsername(uname):
	target_link="http://instagram.com/"+uname+"/"
	response=urllib2.urlopen(target_link)
	page_source=response.read()
	string_start=page_source.find("profilePage_")+12
	return page_source[string_start:string_start+10]
	
print(getIDbyUsername(sys.argv[1]))

	