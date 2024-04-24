#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int width = 5;
	int *mas = NULL;
	mas = malloc(sizeof(*mas) * width);
	for (int i = 0; i < width; i++)
		mas[i] = 10 * i;

	for (int i = 0; i < width; i++)
		fprintf(stdout,"%d ",mas[i]);
	free(mas);
	printf("\n");
	width = 3;
	mas = realloc(mas, sizeof(*mas) * width);
	for (int i = 0; i < width; i++)
		fprintf(stdout,"%d ",mas[i]);
	free(mas);
	return 0;
}
