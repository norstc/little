#!/bin/bash

LIMIT=1
n=1
# use while loop to control
while [ "$n" -lt "$LIMIT" ]
do
echo ${n}
echo ``
let "n += 1"


#wait 10 seconds
sleep 10
done

echo
