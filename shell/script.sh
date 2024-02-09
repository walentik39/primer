#!/usr/bin/env bash

for var1 in 1 2 3 4 5 6 7 8 9 10
do
	if [ $var1 -eq 5 ]
	then
		break
	fi
	echo "цикл работает поскольку значение меньше 5 и равно $var1 "
done
