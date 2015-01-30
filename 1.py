#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

try: print ''.join(str(x) if not x.isalpha() else chr(ord(x) + 2 - 26) if ord(x) + 2 > ord('z') else chr(ord(x) + 2) for x in sys.argv[1])
except(IndexError): print 'No arguments'
