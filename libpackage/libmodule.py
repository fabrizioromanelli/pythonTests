import urllib2
import urllib
import json
import smtplib
import datetime

def apiCallTest1():
	print "test1"

def apiCallTest2():
	print "test2"

#
# Query google for something. Just an exercise.
#
def queryGoogle():
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

#
# Send and email.
#
def sendEmail():
	username   = 'fabrizio.romanelli@gmail.com'
	serverName = 'smtp.gmail.com'
	fromaddr   = 'pilot@mailjet.com'

	toaddrs    = ['fabrizioromanelli@gmail.com']

	logTime = datetime.datetime.now()

	SUBJECT = "New mail!"
	TEXT    = "["+logTime.strftime("%d.%m.%Y %H:%M")+"] - Continuo a dire che ho detto di no!"

	msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

	#try:
	server = smtplib.SMTP_SSL(serverName, 465)
	print("Ehloing the server...")
	server.ehlo("example.com")
	#gPass = raw_input("Please provide your password >> ")
	print("Logging in to the server.")
	server.login(username, password)
	server.mail(fromaddr)
	server.rcpt(toaddrs[0])
	server.data(msg)
#		server.sendmail("jimmy@ridimmi.com", toaddrs[0], msg)
	server.quit()
	print("Email sent!")
	#except:
	#	print("Something went wrong...")
