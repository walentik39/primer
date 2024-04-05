#include <stdio.h>
#include <stdlib.h>

extern int global_var;
extern char global_str[];

int randint(int , int);

int main(void)
{
	int a = 1, b = 10;
	printf("%d\n", randint(a, b));
	printf("%d\n", randint(a, b));
	printf("%d\n", randint(a, b));
	printf("%d\n", randint(a, b));
	printf("%d\n", randint(a, b));
	printf("global_var = %d\n",global_var);
	printf("global_str = %s\n",global_str);
	return 0;
}

char global_str[100] = "Hello";
