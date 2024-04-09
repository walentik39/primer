#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int *mas = NULL;
	int cnt = 4;

	mas = malloc(sizeof(int) * cnt);

	for(int i = 0; i < cnt; i++)
		mas[i] = 123;
	for(int i = 0; i < cnt; i++)
		printf("%d\n",mas+i);

	free(mas);

	return 0;
}

