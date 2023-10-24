#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	short m = -1;
	printf("m = %hd = %hu = 0x%.2hx\n" , m, m, m);

	int n = -1;
	printf("n = %d = %u = 0x%.2x\n", n, n, n);

	long long p = -1;
	printf("p = %lld = %llu = 0x%.2llx\n", p, p, p);
	return 0;
}
