#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i;
	scanf("%d",&i);
	i = 50 + (i < 10 ? 10:i * i); /* если левая часть выполняется, то 10 иначе i * i */
	printf("%d\n", i);
	EXIT_SUCCESS;
}
