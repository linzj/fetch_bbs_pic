import sys
shouldprintDebug = True
def printDebug(s):
    global shouldprintDebug
    if shouldprintDebug:
        print >>sys.stderr,s

def printError(s):
    print >>sys.stderr,s

def setDebug(boolean):
    global shouldprintDebug
    shouldprintDebug = True

def printTest(s):
    print >>sys.stderr,s
