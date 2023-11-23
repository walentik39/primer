#include <stdio.h>
#include <stdlib.h>

void swap(int *px, int *py)
{
	int temp;
	temp = *px;
	*px = *py;
	*py = temp;
}

int main(int argc, char* argv[])
{
	int a = 24;
	int b = 42;
	printf("a = %d\n", a);
	printf("b = %d\n", b);

	swap(&a, &b);
	printf("a = %d\n", a);
	printf("b = %d\n", b);
	return 0;
}
