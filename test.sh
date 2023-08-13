#!/usr/local/bin/bash
set -o errexit
#
set -o nounset # Неоределлёная перменная.
set -u

ls -R
words="А я иду, шагаю по Москве, А я пройти ещё смогу."


echo "Words withous double quotes"
for word in $words; do
	echo "$word"
done
echo


echo "Words withous double quotes"
for word in "$words"; do
	echo "$word"
done
sleep 10; echo -e "Time's up\a"
