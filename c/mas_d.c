#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int *mas = NULL;
	mas = malloc(sizeof(int) * 2);
	*mas = 111;
	*(mas+1) = 444;
	fprintf(stdout,"%d\n",mas[0]);
	printf("%d\n", mas[1]);

	return 0;
}
