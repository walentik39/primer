#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	signed char x = -128; // двоичный 1000 0000
	printf("x = %d\n", x);

	x = x << 1;
	printf("x = %d\n", x);

	x = -128;
	x = x >> 1; 
	printf("x = %d\n", x);		 

	x = x >> 2;
	printf("x = %d\n", x);		 

	x = x >> 1; 
	printf("x = %d\n", x);		 

	x = x >> 1; 
	printf("x = %d\n", x);		 

	x = x << 1; 
	printf("x = %d\n", x);		 

	x = x << 2; 
	printf("x = %d\n", x);		    //
	return 0;
}
