#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	srand(time(NULL));
	int n;
	scanf("%d", &n);
	for (int i = 0; i<n;i++)
		printf("%d\n",i);
	for(int j = n; j>0; j--)
		printf("%d\n",j);
	printf("%d\n", rand());
	return 0;
}

