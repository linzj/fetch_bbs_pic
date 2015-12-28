#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2
import glob, os.path, shutil, os, sys
import pickle
import os.path

help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(20, 20), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return False
    rects[:,2:] += rects[:,:2]
    return True

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

def main(faceset):
    if os.path.exists("faces"):
        if not os.path.isdir("faces"):
            shutil.rmtree("faces")
            os.mkdir("faces")
    else:
        os.mkdir("faces")
    fd(faceset)

def fd(faceset):
    cascade_fn = 'haarcascade_eye_tree_eyeglasses.xml'

    cascade = cv2.CascadeClassifier(cascade_fn)
    for f in glob.glob('*.jpg'):
        if f in faceset:
            continue
        if not os.path.isfile(f):
            continue
        img = cv2.imread(f)
        #print('detecting %s' % f)
        #cv2.imshow('facedetect', img)
        #cv2.waitKey(-1)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        detected = detect(gray, cascade)
        if detected:
            print("%s contains face" % (f))
            shutil.move(f, os.path.join("faces", f))
            faceset.add(f)

def hog(faceset):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )

    for f in glob.glob('*.jpg'):
        if f in faceset:
            continue
        try:
            img = cv2.imread(f)
            if img is None:
                print('Failed to load image file:', fn)
                continue
        except:
            print('loading error')
            continue

        print('detecting %s' % f)
        found, w = hog.detectMultiScale(img, winStride=(8,8), padding=(32,32), scale=1.05)
        if len(found) != 0:
            print("%s contains face" % (f))
            shutil.copy(f, os.path.join("faces", f))
            faceset.add(f)


if __name__ == '__main__':
    faceset = None
    try:
        if os.path.isfile('faceset'):
            with open('faceset', 'rb') as f:
                faceset = pickle.load(f)
    except Exception as e:
        pass
    if not faceset:
        faceset = set()
    main(faceset)
    with open('faceset', 'wb') as f:
        pickle.dump(faceset, f)
