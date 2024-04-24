#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int width = 5;
	int height = 3;
	int *mas = NULL;
	mas = malloc(sizeof(*mas) * width * height);

	for (int j = 0; j < height; j++)
		for (int i = 0; i < width; i++)
			mas[i*width + j] = 100*j+i;


	for (int j = 0; j < height; j++)
		for (int i = 0; i < width; i++)
			printf("%d\t%s",mas[i*width + j],(i == width - 1) ? "\n" : " ");

	free(mas);
	return 0;
}
