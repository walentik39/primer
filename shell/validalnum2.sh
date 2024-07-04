#!/usr/bin/env bash

validAlphaNum()
{
	validchars="$(echo $1 | sed  -e 's/[^[:upper:] ,.]//g')"

	if [ "$validchars" = "$1" ]; then
		return 0
	else
		return 1
	fi
}

/bin/echo -n "Enter input: "
read input


if ! validAlphaNum "$input" ; then
	echo "Please enter only letters and simvols. " >&2
	exit 1
else
	echo "Input is valid. "
fi
exit 0
