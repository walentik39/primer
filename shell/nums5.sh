#!/usr/bin/env bash
var1=11

while [ $var1 -gt 0 ]
do
	echo $var1
	var1=$[var1 - 1]
done
