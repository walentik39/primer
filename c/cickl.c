#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int n ;
	int s = 0 ;

	if(scanf("%d",&n) !=1) {
		printf("Error input!");
		return 0;
	}

	while (n > 0) {
		s += n * n;
		n--;
	}
	printf("s = %d\n", s);

	return 0;
}
