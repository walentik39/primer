#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

extern int randint(int, int);

extern int global_seed_randint;
extern int global_var;

int main(void)
{
	int a = 1, b = 100;
	printf("%d\n", global_seed_randint);
	printf("%d\n", global_var);
	printf("%d\n", randint(a,b));
	printf("%d\n", randint(a,b));
	printf("%d\n", randint(a,b));
	printf("%d\n", randint(a,b));
	return 0;
}
