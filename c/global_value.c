#include <stdio.h>
#include <stdlib.h>

char arr1[] = {0xab, 0xcd, 0xef};
short arr2[] = {0x1234, 0x5678, 0xabcd};

int main(int argc, char* argv[])
{
	printf("arr1: 0x%p\n", arr1);
	printf("arr2: 0x%p\n", arr2);
	EXIT_SUCCESS;
}
