#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	unsigned char x = 40; // двоичная запись 00101000
	printf("x = %d\n", x);

	x = x >> 1; //число 20 00010100
	printf("x = %d\n", x);		 

	x = x >> 2; //число 5 00000101
	printf("x = %d\n", x);		 

	x = x >> 1; //число 2 00000010
	printf("x = %d\n", x);		 

	x = x >> 1; //число 1 00000001
	printf("x = %d\n", x);		 

	x = x << 1; //число 2 00000010
	printf("x = %d\n", x);		 

	x = x << 2; //число 8 00001000
	printf("x = %d\n", x);		    //
	return 0;
}
