#include <stdio.h>
#include <stdlib.h>

int gcd(int a, int b)
{
	if (0 == b)
		return a;
	return gcd(b, a%b);
}
int main(int argc, char* argv[])
{
	int n, m;
	scanf("%d%d", &n, &m);
	printf("gcd(%d,%d) = %d\n", n, m, gcd(n, m));
	return 0;
}
