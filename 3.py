#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2, re

source = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()

print ''.join(re.findall('(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])', source))
