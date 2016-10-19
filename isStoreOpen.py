#Adapted using documentation from https://docs.python.org/2/howto/urllib2.html
#Written by Nick McComb | www.nickmccomb.net
#Written in October 2016

import urllib2
import time

print "Welcome to the resi.STORE monitoring system!"

while 1:
	req = urllib2.Request('http://osurobotics.club/web_scripts/lux.bool')
	response = urllib2.urlopen(req)
	the_page = response.read()

	if the_page[0] == "0":
		print "The resiSTORE is not open :("
	else:
		print "The resiSTORE is open!"
	time.sleep(10)