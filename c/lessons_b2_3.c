#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	unsigned char flags = 13; // двоичная запись 00001101
	unsigned char mask = 5; // двоичная запись 00000101
	flags = flags & ~mask;	  
	printf("flags = %d\n",flags);
	return 0;
}
