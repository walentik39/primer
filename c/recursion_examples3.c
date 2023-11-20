#include <stdio.h>
#include <stdlib.h>

double fast_power(double a, int n)
{
	if (0 == n)
		return 1;
	if (n%2 == 1)
		return a*fast_power(a, n-1);
	else
		return fast_power(a*a, n/2);
}
int main(int argc, char* argv[])
{
	int n, m;
	scanf("%d%d", &n, &m);
	printf("fast_power(%d,%d) = %lf\n", n, m, fast_power(n, m));
	return 0;
}
