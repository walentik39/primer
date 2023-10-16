#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char x;
	for (x=0;x < 10;x++)
	{
		printf("+\n");
		for(char i = x;i < 10;i++)
			printf("#\n");
	}
	return 0;
}
