#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	FILE *even, *odds;
	int n;
	size_t k = 0;
	scanf("%d",&n);

	even = fopen("even.txt", "w");
	odds = fopen("odds.txt","w");

	for (k = 1; k < n + 1; k++)
	{
		k%2==0 ? fprintf(even, "\t%5d\n", k)
			: fprintf(odds, "\t%5d\n", k);
	}
	fclose(even);
	fclose(odds);
	for (k = 1; k < n + 1; k++)
	{
		k%2==0 ? printf("Чётное число \t%5d\n", k)
			: printf("Нечётное число \t%5d\n", k);
	}


	EXIT_SUCCESS;
}
