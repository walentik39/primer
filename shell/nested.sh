#!/usr/bin/env bash
#nested is example

read -p "Enter the first num: " n1
read -p "Enter the second num: " n2
read -p "Enter the third num: " n3

if [[ $n1 -ge $n2 ]]; then
if [[ $n1 -ge $n3 ]]; then
echo "$n1 is the greater number "
else
	echo "n3 is the greater number "
fi
else
if [[ $n2 -ge $n3 ]]; then
echo "$n2 is greater "
else
	echo "$n3 is greater "
fi
fi
