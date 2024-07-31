#!/usr/bin/env bash
#Сценарий сбора информации

#команда 1
function uname_func ()
{
	UNAME="uname -a"
	printf "Gathering system information with the $UNAME command: \n\n"
	$UNAME
}

#Команда 2
function disk_func ()
{
	DISKSPACE="df -h"
	printf "Gathering diskspace information with the $DISKSPACE command:
	\n\n"
	$DISKSPACE
}

function main ()
{
	uname_func
	disk_func
}
main
