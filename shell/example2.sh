#!/usr/bin/env bash

echo "Enter x number"
read x

echo "Enter y number"
read y

if [ $x -ne $y ]
then
	echo X is not equal to Y
elif [ $x -eq $y ]
then
	echo X is equal to Y
fi

