#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char m = 0b01111111;
	printf("m = %d\n", m); // 127
	m = m + 1;
	printf("m = %d\n", m); //-128
	return 0;
}
