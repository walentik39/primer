#include <stdio.h>
#include <stdlib.h>

//фибоначи

void swap_2(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

int main(int argc, char* argv[])
{
	int x = 0;
	int y = 1;
	int n;
	scanf("%d", &n);
	while (x < n)
	{
		printf("%d\n", x);
		swap_2(&x, &y);
		x += y;
		x++;
	}


	EXIT_SUCCESS;
}

