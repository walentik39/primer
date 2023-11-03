#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int * create_arr()
{
	srandom(2);
	int * arr = malloc(sizeof(int) * 5);
	arr[0] = 3;
	arr[1] = 5;
	arr[2] = 7;
	arr[3] = rand();
	arr[4] = rand();
	return arr;
}
int main(int argc, char* argv[])
{
	int * a = create_arr();

	for (int i = 0; i < 5; i++)
		printf("a[%d] = %d\n", i, a[i]);
	free(a);
	return 0;
}
