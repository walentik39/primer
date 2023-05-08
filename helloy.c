#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	int x;
	int y;
	printf("Введём значения x и y \n");
	scanf("%d", &x);
	scanf("%d", &y);
	printf("результат = %d \n", x + y);
	return 0;
}
