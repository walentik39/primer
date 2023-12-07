#include <stdio.h>
#include <stdlib.h>

short word1 = 0;
int lword2;

int main(int argc, char* argv[])
{
	printf("word1: addr = 0x%p, value = %hx\n", &word1, word1);
	printf("lword2: addr = 0x%p, value = %x\n", &lword2, lword2);
	EXIT_SUCCESS;
}
