#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int *mas = NULL;

	mas = malloc(sizeof(int) * 2);
	*mas = 444;
	*(mas+1) = 777;
	free(mas);
	mas = malloc(sizeof(int) * 3);

	printf("%d\n",mas[0]);
	printf("%d\n",mas[1]);

	free(mas);

	return 0;
}
