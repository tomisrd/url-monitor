#!/usr/bin/env python3
# Description : url-monitor.py is a simple script that monitors the HTTP code of a passed website
# HTTP codes verified -> 200, 401, 403, 404
# Author: tomisrd



import requests

# creating my list
my_list_of_website= ['http://google.com/','https://www.youtube.com/','https://twitter.com/login','https://www.twitch.tv/']

# url definition
url = "http://google.com"

# request url and get status code
r=requests.head(url)
status_code = r.status_code

# request status code check
# 200
if status_code == 200:
	print(url + " is up - " + str(status_code))
# 301
elif status_code == 301:
	print(url + " is redirected - " + str(status_code))
# 302
elif status_code == 302:
	printf(url + " is found - " + str(status_code))
# 401
elif status_code == 401:
	print(url + " is unauthorized - " + str(status_code))
# 403
elif status_code == 403:
	printf(url + " is forbidden - " +str(status_code))
# 404
elif status_code == 404:
	print(url + " is down - " + str(status_code))

