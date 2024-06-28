#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int s = 0;
	int x;

	while(scanf("%d",&x) == 1 && x !=0)
		s+=x;
	printf("s = %d\n", s);

	return 0;
}
