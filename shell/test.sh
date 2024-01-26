#!/usr/bin/env bash

set -eEx

arr=$(ls -al ~/*)

echo "all items"
printf "%s\n" "${arr[@]}"
