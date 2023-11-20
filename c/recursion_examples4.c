#include <stdio.h>
#include <stdlib.h>

int fib(int n)
{
	if (n <= 1)
		return n;
	else
		return fib(n-1) + fib(n-2);
}
int main(int argc, char* argv[])
{
	int n;
	scanf("%d", &n);
	printf("fib(%d) = %d\n", n, fib(n));
	return 0;
}
