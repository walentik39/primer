#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char m = -100;
	printf("m = %d\n", m); // 1
	m = ~m ;   // по битовое отрицание
	m = m + 1; 
	printf("m = %d\n", m); 
	return 0;
}
