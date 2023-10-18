#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	short x = 0xabcd;
	long long addr = (long long)&x;
	short * addr2 = &x;
	char s = sizeof(addr2);
	printf("%p\n", addr);
	printf("\nsize of addr2: %d", s);
	return 0;
}
