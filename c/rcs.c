#include <stdio.h>
#include <stdlib.h>

void rcs(int x)
{
	printf("Down: c = %d\n", x); /* прямая рекурсия */

	if(x > 1)
		rcs(x-1);
	
	printf("Up: x = %d\n", x); /* обратная рекурсия */
}

int main(void)
{
	int x;
	scanf("%d", &x);
	rcs(x);

	return 0;
}
