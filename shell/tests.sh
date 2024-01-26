#!/usr/bin/env bash

declare -A arr

arr[key1]="val1"
arr[key2]="val2"
arr[key3]="val3"


for key in ${!arr[@]}; do
	echo "$key: ${arr[$key]}"
done	

unset arr[key1]

echo "------------"

for key in ${!arr[@]}; do
	echo "$key: ${arr[$key]}"
done	
