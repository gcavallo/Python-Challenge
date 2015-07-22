#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2, re, bz2

data = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').read()
print '\n'.join(bz2.decompress(i.decode('string_escape')) for i in re.findall('\w{2}: \'(.*?)\'', data))
