#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	short x = 0xabcd;
	long long addr1 = (long long)&x;
	short * addr2 = &x;
	printf("addr1: %p\n", addr1);
	printf("addr2: %p\n", addr2);
	return 0;
}
