#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  check.py
#  
#  Copyright 2021 Ali Morakabi <alimkb@gmail.com>
#  
#  
import json,smtplib,ssl
import urllib.request

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




def sendAlert(website,keyword):
	
	port = 465  # For SSL
	smtp_server = "mail.MAILSERVER.com"
	sender_email = "admin@YOURDOMAIN.com"  # Enter your address
	receiver_email = "alimkb@gmail.com"  # Enter receiver address
	password = 'password' # Enter your email apssword
	
	message = MIMEMultipart("alternative")
	message["Subject"] = "Website monitor Alert!"
	message["From"] = sender_email
	message["To"] = receiver_email
	# write the plain part
	#text = ""
	# write the HTML part
	html = f"""\
	<html>
	  <body>
	    <p>Hi,<br>
	       The keyword {keyword} doest not exists , Please check the status for :</p>
	    <p><a href="{website}">{website}</a></p>
	    <p> Feel free to <strong>let us</strong> know what alert type would be useful for you!</p>
	  </body>
	</html>
	"""
	# convert both parts to MIMEText objects and add them to the MIMEMultipart message
	#part1 = MIMEText(text, "plain")
	part2 = MIMEText(html, "html")
	#message.attach(part1)
	message.attach(part2)

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message.as_string())
	    





url = ''
resp = ''
content = ''
req = ''
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
	
f = open('sites.json','r')
data = json.load(f)
	
for i in data['websites']:
		
	try:
		url = i['url']
		req = urllib.request.Request(url, headers = headers )
		resp = urllib.request.urlopen(req, timeout=10)			
		content = resp.read()
			
			
		if i['keyword'] in str(content):
			print(f"{i['name']} is Alive!")
		else:
			print(f"{i['name']} is not available!")
			sendAlert(i['url'],i['keyword'])
	except Exception as e:
			
		print(str(e))
