#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re, zipfile

nothing = "90052"
comments = []

while nothing.isdigit():
	zf = zipfile.ZipFile('channel.zip', 'r')
	content = zf.open('{0}.txt'.format(nothing)).read()
	print content
	info = zf.getinfo('{0}.txt'.format(nothing))
	comments.append(info.comment)
	try:
		nothing = re.search('(?<=Next nothing is )(\d+)', content).group(0)
	except:
		break

print ''.join(comments)
