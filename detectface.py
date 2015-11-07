#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2
import glob, os.path, shutil, os

help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return False
    rects[:,2:] += rects[:,:2]
    return True

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    cascade_fn = 'haarcascade_frontalface_alt.xml'

    cascade = cv2.CascadeClassifier(cascade_fn)
    if os.path.exists("faces"):
        if not os.path.isdir("faces"):
            shutil.rmtree("faces")
            os.mkdir("faces")
    else:
        os.mkdir("faces")

    for f in glob.glob('*.jpg'):
        if not os.path.isfile(f):
            continue
        img = cv2.imread(f, 0)
        #cv2.imshow('facedetect', img)

        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(img)

        detected = detect(gray, cascade)
        if detected:
            print("%s contains face" % (f))
            shutil.move(f, os.path.join("faces", f))

