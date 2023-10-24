#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	for(int i = 0; i < 7; i++)
		for(int j=i;j<7;j++)
		{
			printf("%d\t %d\n",i, j);
			putchar('\n');
		}
		putchar(37);
		putchar('\n');
	return 0;
}
