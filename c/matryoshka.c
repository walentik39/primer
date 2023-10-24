#include <stdio.h>
#include <stdlib.h>

void matryoshka(int n);

int main(int argc, char* argv[])
{
	matryoshka(7);

	EXIT_SUCCESS;
}

void matryoshka(int n)
{
	if (n == 1)
		printf("Last Matryoshka %d\n", n);
	else
	{
		printf(" Top side of matryoshka %d\n", n);
		matryoshka(n-1);
		printf("Bottom side of matryoshka %d\n", n);
	}
}
