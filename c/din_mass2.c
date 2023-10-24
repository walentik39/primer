#include <stdio.h>
#include <stdlib.h>


int main(int argc, char* argv[])
{
	int N;
	printf("Enter size of array to create:");
	scanf("%d", &N);

	char *A = (char*)malloc(N);
	if (NULL == A)
	{
		printf("Os didnt't gave memory. Exit..\n");
		exit(1);
	}
	for (int i =0; i < N;++i)
		A[i] = i;

	printf("Array successfully created:\n");

	return 0;
}
