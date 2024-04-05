#include <stdlib.h>

int global_var = 5;

int global_seed_randint = 0;

int randint(int a, int b)
{
	int right = a, left = b;
	if(a > b) {
		right = b;
		left = a;
	}

	return rand() % (left - right + 1) + right;
}
