#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import urllib2, base64, re

request = urllib2.Request('http://www.pythonchallenge.com/pc/return/good.html')
login = base64.encodestring('{0}:{1}'.format('huge', 'file')).replace('\n', '')
request.add_header('Authorization', 'Basic {0}'.format(login))
source = re.split('first:|second:', urllib2.urlopen(request).read())

first = zip(*[iter(int(i) for i in re.findall('\d{1,3}', source[1]))]*2)
second = zip(*[iter(int(i) for i in re.findall('\d{1,3}', source[2]))]*2)

im = Image.new('RGB', (512,512), (255,255,255))
draw = ImageDraw.Draw(im)
draw.line(first, fill=(128,64,32), width=2)
draw.line(second, fill=(96,32,0), width=3)
im.show()
