#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	unsigned char flags = 5; // двоичная запись 00000101
	unsigned char mask = 4; // результат 01100100
	if( (flags & mask) == mask)			  
		printf("bit 2 is on");
	else
		printf("bit 2 is off");
	return 0;
}
