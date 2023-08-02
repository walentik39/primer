#!/usr/local/bin/bash
#
PREFIX=ARG

for arg in "$@"
do
	echo "${PREFIX}: $arg"
	#continue
	if [ -f "$arg" ] ; then
		echo "${arg} is a file"
	elif [ -d "$arg" ] ; then
		echo "${arg} is a dir"
	elif [ -L "$arg" ] ; then
		echo "${arg} is a link"
	fi
done
