#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char m = 5;
	char n = 7;
	char p = m < n;
	printf("p = %d\n", p);
	char s = (m < n) && (n < 10);
	printf("s = %d\n", s);
	EXIT_SUCCESS;
}
