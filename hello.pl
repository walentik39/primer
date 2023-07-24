#!/usr/bin/perl
#
print "Ваше имя?\n";
$name = <STDIN>;

$~ = NAME_FORMAT;
write;

$~ = NAME_FORMAT_BOTTOM;
write;

format NAME_FORMAT=
Привет, @>>>>>>>>>>>>>>>>>!
$name
.

format NAME_FORMAT_TOP=
==========================
.

format NAME_FORMAT_BOTTOM=
=============================
.
