#!/usr/bin/env bash

for ((var1=1; var1 < 20; var1++))
do
	if [ $var1 -gt 5 ] && [ $var1 -lt 15 ]
	then continue
	fi
	echo "$var1"
done
