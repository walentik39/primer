#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int func(int a, int b)
{

	int x;
	int y;
	printf("Введём значения x и y \n");
	scanf("%d", &x);
	scanf("%d", &y);
	fprintf(stdout,"%d\n", x + y);
}

int main(int argc, char* argv[])
{
	int res;
	res = func(random(),random());
	printf("%d %d\n",res);
	return 0;
}
