#!/usr/bin/env python3
import os, sys
import glob
from PIL import Image

images = glob.glob('/home/student-02-ddf722693a09/images/*')
root = os.getcwd()
for infile in images:
    f, e = os.path.splitext(infile)
    src = os.path.join(root, infile)
    with Image.open(infile) as im:
        print(infile, im.format, "%dx%d" % im.size, im.mode)
        name = "/opt/icons/"+str(os.path.basename(infile))+'.jpg'
        print(name)
        im.convert('L').rotate(90).resize((128,128)).save(name)
        print(im, im.format, "%dx%d" % im.size, im.mode)
