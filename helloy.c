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
	fprintf(stdout,"%4f\n", sqrt(x + y));
}

int main(int argc, char* argv[])
{
	float n,m,res;
	printf("Введите значения n и m \n");
	scanf("%4f",&n);
	scanf("%4f",&m);
	res = sqrt(n + m);
	func(n,m);
	printf("%4f\n",res);
	return 0;
}
