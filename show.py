#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2
import glob, os.path, shutil, os, sys

help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(20, 20), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return rects
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

def main():
    fd()

def fd():
    cascade_fn = 'haarcascade_eye_tree_eyeglasses.xml'

    cascade = cv2.CascadeClassifier(cascade_fn)

    for f in glob.glob(sys.argv[1]):
        if not os.path.isfile(f):
            continue
        img = cv2.imread(f)
        print('detecting %s' % f)
        #cv2.imshow('facedetect', img)
        #cv2.waitKey(-1)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        detected = detect(gray, cascade)
        if len(detected) != 0:
            print("%s contains face" % (f))
            draw_rects(img, detected, (255, 0, 0, 255))
            cv2.imshow('img',img)
            cv2.waitKey(0)

if __name__ == '__main__':
    main()
