#!/usr/local/bin/bash

echo "pid is $$"
while (( COUNT < 12 ))
do
	sleep 3
	(( COUNT ++ ))
	echo $COUNT
done
exit 0
