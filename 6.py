#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re, zipfile

nothing = "90052"
comments = []

while nothing.isdigit():
	content = open('channel/' + nothing + '.txt').read()
	print content
	zf = zipfile.ZipFile('channel.zip', 'r')
	info = zf.getinfo(nothing + '.txt')
	comments.append(info.comment)
	try:
		nothing = re.search('(?<=Next nothing is )(\d+)', content).group(0)
	except:
		break

print ''.join(comments)
