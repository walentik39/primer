#include <stdio.h>
#include <stdlib.h>
#define ARRAY_LENGTH 10

int main(int argc, const char* argv[])
{
	int size = 5;
	int numbers[5] = {1, 8, 3, 2, 6};
	int current_index = 0;
	int max_number_index = 0;
	int max = numbers[0];
	while(current_index < size)
	{
		if(numbers[current_index] > max)
			max = numbers[current_index];
			max_number_index = current_index;
		current_index = current_index + 1;
	}
	current_index = 0;
	int second_max = numbers[0];
	if(max_number_index == 0)
		second_max = numbers[1];
	while(current_index < size)
	{
		if(current_index != max_number_index)
			if(numbers[current_index] > second_max)
				second_max = numbers[current_index];
		current_index = current_index + 1;
	}
	printf("%d\n", second_max);
}
