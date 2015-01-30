#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2, re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"

while nothing.isdigit():
	response = urllib2.urlopen(url + nothing).read()
	print response
	try:
		nothing = re.search('(?<=the next nothing is )(\d+)', response).group(0)
	except:
		if 'Divide by two' in response:
			nothing = str(int(nothing) / 2)
		else:
			break
