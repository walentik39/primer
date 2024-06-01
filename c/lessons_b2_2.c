#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	unsigned char flags = 1; // двоичная запись 00000001
	unsigned char mask = 4; // двоичная запись 00000100
	if( (flags & mask) == mask)			  
		printf("bit 2 is on");
	else
		printf("bit 2 is off");
	return 0;
}
