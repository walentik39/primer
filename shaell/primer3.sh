#!/usr/bin/env bash

arr=$(ls -a ~/*)

echo "all items"
printf "%s\n" "${arr[@]}"
