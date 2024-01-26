#!/usr/bin/env bash

projectPatches=".config;primer;.cache"

IFS=";" read -a PD <<< "$projectPatches"
targets=()

for i in "${PD[@]}"; do
	targets+=($(exa -d $HOME/$i/*))
done

printf "%s\n" "${targets[@]}"

targetDir=$(printf "%s\n" ${targets[@]} | fzf)

if [ -d "$targetDir" ]
then
	echo "$targetDir is picked"
else
	echo "$targetDir is not directory"
	exit 1
fi	

