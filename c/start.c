#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
	int n, i,j; /* количество звёздочек */
	scanf("%d",&n);
	for (i=0; i < n; i++)
	{
		for(j=0; j<i; j++)
			printf(" ");
		for(j=n-i; j>0;j--)
			printf("*");
			printf("\n");
	}

	EXIT_SUCCESS;
}	
