#!/usr/bin/env bash
file="/var/log"
IFS=$'\n'
for warrior in $(ls -l $file)
do
	echo $warrior 
done	

