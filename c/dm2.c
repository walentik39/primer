#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	int * a = calloc(3, sizeof(int));
	a[0] = 3;
	a[1] = 5;
	a[2] = 7;
	int * a1 = malloc(5 * sizeof(int));
	memcpy(a1, a, 3 * sizeof(int));
	free(a);
	a = a1;
	a[3] = 11;
	a[4] = 15;
	for (int i = 0; i < 5; i++)
		printf("a[%d] = %d\n", i, a[i]);
	free(a);
	return 0;
}
