#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char m = 0b00000001;
	printf("m = %d\n", m); // 1
	m = ~m ;   // 0b11111110 по битовое отрицание
	m = m + 1; // 0b11111111
	printf("m = %d\n", m); 
	return 0;
}
