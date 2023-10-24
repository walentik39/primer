#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char m = 8;
	char n = 6;
	if(m > n)  //если это условие выполняется
	{
		printf("m > n, %d > %d\n", m, n);
	}
	else   //иначе выполняется это
	{
		printf("m <= n, %d <= %d\n", m, n);
	}
	return 0;
}
