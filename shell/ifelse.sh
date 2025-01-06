#!/usr/bin/env bash
#if statement example
read -p "What is your age: " age
if [ $age -lt 18 ]; then
	echo "You are no elgible for voting"
else
	echo "Вы не плохо держитесь "
fi
