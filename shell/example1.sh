#!/usr/bin/env bash

echo "Enter x number"
read x

echo "Enter y number"
read y

if [ $x -gt $y ]
then
	echo X is greater than Y
elif [ $x -le $y ]
then
	echo X Less than equal to Y
fi

