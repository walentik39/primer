#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	unsigned char var = 153; // двоичная запись 10011001
	unsigned char not_v = ~var; // результат 01100110 (число 102)
	printf("var = %d, not_v = %d\n", var, not_v);
	return 0;
}
