#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	int lword = 0x1234abcd;
	short * p = (short *)&lword;
	printf("lword: value = 0x%hx, addr = 0x%p\n", lword, &lword); 
	printf("low word = 0x%hx", *p); 
	return 0;
}
