#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2, re

source = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read().rstrip('\r\n')
text = re.findall('<!--(.*?)-->', source, re.DOTALL)[1]

print ''.join(x for x in text if x.isalpha())
