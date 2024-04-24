#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int width = 5;
	int height = 3;
	int **mas = NULL;
	mas = malloc(sizeof(*mas) * width);
	for (int i = 0; i < width; i++)
		mas[i] = malloc(sizeof(**mas) * height);
	

	for (int j = 0; j < height; j++)
		for (int i = 0; i < width; i++)
			mas[i][j] = 100*j+i;

	height = 4;
	for (int i = 0; i < width; i++)
		mas[i] = realloc(mas[i], sizeof(**mas) * height);

	for (int j = 0; j < height; j++)
		for (int i = 0; i < width; i++)
			printf("%d\t%s",mas[i][j],(i == width - 1) ? "\n" : " ");

	for (int i = 0; i < width; i++)
		free(mas[i]);
	free(mas);
	return 0;
}
