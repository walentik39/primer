#!/usr/bin/env bash

IFS=:
for FOLDER in $PATH
do
	echo "$FOLDER:" >> log.odt
	for file in $FOLDER/*.*
	do
		if [ -x $file ]
		then
			echo " $file" >> log.odt
		fi
	done
done
