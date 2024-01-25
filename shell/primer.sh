#!/usr/bin/env bash

arr=("one" "two" 10 55 [100]="ff")

printf "%s\n" ${arr[@]}

echo ${!arr[@]}

echo ${#arr[@]}
