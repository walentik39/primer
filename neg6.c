#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char m = -128;
	short n = -128;
	printf("m = %d\n", m); // -128
	printf("n = %d\n", n); // -128
	m = ~m ;   // по битовое отрицание
	m = m + 1; 
	n = ~n;
	n = n + 1;
	printf("m = %d\n", m);
        printf("n = %d\n", n);	
	return 0;
}
