#include <stdio.h>
#include <stdlib.h>
#define ARRAY_LENGTH 10

int main(int argc, const char* argv[])
{
	int arr[ARRAY_LENGTH];
	int i = 0;
	float result = 0;
	while(i<ARRAY_LENGTH){
		printf("Введите число %d\n", i);
		scanf("%d", arr + i);
		i++;
	}

	printf("Our array is:");
	for(i = 0;i < ARRAY_LENGTH;i++)
		printf("%d ", arr[i]);
	printf("\n And the average is : ");
	for(i = 0;i < ARRAY_LENGTH;i++)
		result += *(arr +i);

	printf("%f \n", result /ARRAY_LENGTH);
}

