#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
	srandom(10);
	int * a = calloc(3, sizeof(int));
	a[0] = 3;
	a[1] = 5;
	a[2] = 7;
	a = realloc(a, sizeof(int) * 5);
	a[3] = 11;
	a[4] = 15;
	for (int i = 0; i < 5; i++)
		printf("a[%d] = %d\n", i, a[i]);
	free(a);
	return 0;
}
