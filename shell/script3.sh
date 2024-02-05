#!/usr/bin/env bash
file="test.odt"
IFS=$'\n'
for warrior in $(cat $file)
do
	echo $warrior 
done	

