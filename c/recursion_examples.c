#include <stdio.h>
#include <stdlib.h>

int factorial(int n)
{
	if (0 == n)
		return 1;
	return factorial (n-1) * n;
}
int main(int argc, char* argv[])
{
	int n;
	scanf("%d", &n);
	printf("factorial(%d) = %d\n", n, factorial(n));
	return 0;
}
