#!/usr/bin/env bash

for ((i=0; i<=4; i++))
do
	echo "Начат цикл с номер $i"
	for ((j=i; j<12; j++))
	do
		echo "продолжен цикл $j"
	done

done
