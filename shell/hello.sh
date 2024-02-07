#!/usr/bin/env bash

for file in /var/log/*
do
if [ -d "$file" ]
	then
		echo "$file Это папка(директория)"
elif [ -f "$file" ]
	then
		echo "$file это файл"
fi
done	

