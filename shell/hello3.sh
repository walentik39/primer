#!/usr/bin/env bash

read -p "Выберете папку : " 

for file in $REPLY
do
	if [ -d "$file" ]
	then
		echo "$file это папка(директория)"
	elif [ -f "$file" ]
	then
		echo "$file это файл"
	fi
done	
