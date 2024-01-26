#!/usr/bin/env bash

projectPatches=".config;primer;.cache"

IFS=";" read -a PD <<< "$projectPatches"
targets=()

for i in "${PD[@]}"; do
	targets+=($(exa -d $HOME/$i/*))
done

printf "%s\n" "${targets[@]}"
