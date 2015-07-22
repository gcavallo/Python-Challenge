#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2, pickle, re

source = pickle.loads(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read())
text = ''.join(x*y for i in source for x,y in i)
print re.sub("(.{95})", "\\1\n", text)
