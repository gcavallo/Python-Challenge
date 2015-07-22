#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from PIL import Image
import re

im = Image.open('oxygen.png')
im = im.crop((4,43,608,44))

text = ''.join(chr(im.getpixel((i, 0))[0]) for i in range(0, im.size[0], 7))
print text, '\n', ''.join(chr(int(i)) for i in re.findall('\d+', text))
