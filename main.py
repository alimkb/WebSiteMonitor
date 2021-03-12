#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2021 Ali Morakabi <alimkb@gmail.com>
#  
#  
import json
import urllib.request



def main(args):
    return 0


def loadJson():
	# Opening JSON file 
	f = open('sites.json',) 
	  
	# returns JSON object as  
	# a dictionary 
	data = json.load(f) 
	  
	# Iterating through the json 
	# list 
	for i in data['websites']: 
	    print("Name : " + i["name"])
	    print("URL  : " + i["url"])
	    print("Keyword : " + i["keyword"]) 
	    print(" ")
	  
	# Closing file 
	f.close() 

def addJson(website):
	# load json data into dictionary
	f = open('sites.json','r+')
	data = json.load(f)
	f.truncate(0)
	
	# append new key values to data
	data['websites'].append({
	    'name': website['name'],
	    'url': website['url'],
	    'keyword': website['keyword']
	})
	# write data to json file
	with open('sites.json', 'a') as outfile:
	    json.dump(data, outfile, indent=4)	
	
	

	
def monitor():
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
		except Exception as e:
			
			print(str(e))
	

def newWebiste():
	data = {}
	num = 0
	print("\n1) add a webiste.")
	print("2) delete website record.")
	print("3) return to main menu.")
	cmd = input("Choose an option : ")
	if cmd == '1':
		data['name'] = input('Enter name of website : ')
		data['url'] = input('Enter URL of website : ')
		data['keyword'] = input('Enter keyword : ')
		addJson(data)
		print('Successfully added!')
		menu()
		
	elif cmd == '2':
		nam = input('Enter name of website you want to delete : ')
		f = open('sites.json','r')
		data = json.load(f)
		
		for i in range(len(data['websites'])):
			
			if data['websites'][i]['name'] == nam :
				del data['websites'][i]
				with open('sites.json', 'w') as outfile:
					json.dump(data, outfile, indent=4)
				break

				
				
			
		
	else :
		pass
		
	
def menu():
	print("\n1) Run website monitor.")
	print("2) Add/delete websites.")
	print("3) Exit .") 
	cmd = input("Choose program mode :")
	
	if cmd == "1":
	    monitor()
	elif cmd == "2":
	    newWebiste()
	elif cmd == "3":
	    exit()
	else:
	    print("Wrong option selected!")
	    menu()
	    
	 

#if __name__ == '__main__':
#    import sys
#    sys.exit(main(sys.argv))

menu()
