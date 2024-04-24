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

	int oldWidth = width;
	width = 4;
	if(oldWidth > width)
	{
		for (int i = width; i < oldWidth; i++)
			free(mas[i]);
		mas = realloc(mas,sizeof(*mas) * width);
	}
	if(oldWidth < width)
	{
		mas = realloc(mas, sizeof(*mas) * width);
		for (int i = oldWidth; i < width; i++)
			mas[i] = malloc(sizeof(**mas) * height);
	}


	for (int j = 0; j < height; j++)
		for (int i = 0; i < width; i++)
			printf("%d\t%s",mas[i][j],(i == width - 1) ? "\n" : " ");

	for (int i = 0; i < width; i++)
		free(mas[i]);
	free(mas);
	return 0;
}
