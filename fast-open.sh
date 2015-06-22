#!/bin/sh
LINE=`grep $1 downloaded.log`
if [ -z "$LINE" ]
    then
        echo "fails to find" >2
fi
host=`echo $LINE| sed -r -e 's/^.*host: ([^,]+).*/\1/'`
path=`echo $LINE| sed -r -e 's/^.*path: ([^,]+).*/\1/'`
gnome-open "http://$host/$path"
