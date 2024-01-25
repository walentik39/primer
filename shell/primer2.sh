#!/usr/bin/env bash

arr=("one" "two" 10 55 [100]="ff")

echo "all items"
for i in ${!arr[@]}; do
	echo ${arr[i]}
	echo $i
done
