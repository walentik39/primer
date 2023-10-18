#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	short x = 0xabcd;
	long long addr1 = (long long)&x;
	short * addr2 = &x;
	printf("addr1: %d\n", addr1);
	printf("addr2: %d\n", addr2);
	addr1 = addr1 + 1;
	addr2 = addr2 + 1;
	printf("addr1: %d\n", addr1);
	printf("addr2: %d\n", addr2);
	addr2 = addr2 + 4;
	printf("addr1: %d\n", addr1);
	printf("addr2: %d\n", addr2);
	return 0;
}
