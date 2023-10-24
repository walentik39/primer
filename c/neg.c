#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	signed char m = 0b11111111;
	unsigned char n = 0b11111111;
	char c1 = m > 0;
	char c2 = n > 0;
	printf("m > 0: %d\n", c1);
	printf("n > 0: %d\n", c2);
	return 0;
}
