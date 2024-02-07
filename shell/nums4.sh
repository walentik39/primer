#!/usr/bin/env bash

for ((i=0; i<=4; i++))
do
	echo "Начат цикл с номер $i"
	for ((j=1; j<4; j++))
	do
		echo "внутренний цикл $j"
	done

done
