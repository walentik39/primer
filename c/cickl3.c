#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int s = 0;
	int n;
	if(scanf("%d",&n) !=1) {
		printf("Error input");
		return 0;
	}
	int i = 0;

	while(++i <= n && i <=10)
			s+=i * i;
	printf("s = %d\n", s);

	return 0;
}
