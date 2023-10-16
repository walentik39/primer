#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char m = 8;
	char n = 6;
	char p = (m > n);
	if(p)  //если p отлично от нуля
	{
		printf("m > n, %d > %d\n", m, n);
	}
	else   //иначе (если p равно нулю)
	{
		printf("m < n, %d < %d\n", m, n);
	}
	return 0;
}
