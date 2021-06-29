#!/usr/bin/env python3
# Description : url-monitor.py is a simple script that monitors the HTTP code of a passed website
# HTTP codes verified -> 200, 401, 403, 404
# Author: tomisrd



import requests


def count_url_letters(url):
	print(len(url))



def check_url_http_status_code(url):

	# Request url and get status code
	r=requests.head(url)
	status_code = r.status_code

	# Request status code check
	# 200
	if status_code == 200:
		print(url + " is up - " + str(status_code))
	# 301
	elif status_code == 301:
		print(url + " is redirected - " + str(status_code))
	# 302
	elif status_code == 302:
		print(url + " is found - " + str(status_code))
	# 401
	elif status_code == 401:
		print(url + " is unauthorized - " + str(status_code))
	# 403
	elif status_code == 403:
		print(url + " is forbidden - " +str(status_code))
	# 404
	elif status_code == 404:
		print(url + " is down - " + str(status_code))

# Creating my list
my_list_of_website= ['https://google.com/','https://www.youtube.com/','https://twitter.com/login','https://www.twitch.tv/']

# Loop through my_list_of_website 
for urls in my_list_of_website:
	check_url_http_status_code(urls)
	count_url_letters(urls)

