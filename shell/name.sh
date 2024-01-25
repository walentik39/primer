#!/usr/local/bin/bash

set -eExu

echo -n "Введите своё имя: "
read user_name

if [ -n "$user_name" ]; then
	echo "Привет! $user_name!"
	exit 0
else
	echo "Вы не назвали своего имени!"
	exit 1
fi	

