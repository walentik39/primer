#!/usr/bin/env bash

IFS=:
FUNC=$(lsof -i)
for FOLDER in $FUNC
do
	echo "$FOLDER:" >> testing.md
	for file in $FOLDER/*.*
	do
		if [ -x $file ]
		then
			echo " $file" >> testing.md
		fi
	done
done
