#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	for (int i = 0;i <12; ++i)
		for (int j = i; j > 0; j--)
		{
			printf("%d, %d\n",i, j);
		}
	printf("Hello , World!\n");
	return 0;
}
