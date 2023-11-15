#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define ARRAY_LENGTH 50
#define NUMBERS_AMOUNT 1000000
int main(int argc, const char* argv[])
{
/*      int array1[ARRAY_LENGTH];
	array1[0] = 10;
	array1[1] = 20;
	int array2[5] = {1, 8, 2, 6, 3};
*/
	srand(time(NULL));
	int frequency[ARRAY_LENGTH] = {0};
	int a, i;
	for(i =0; i< NUMBERS_AMOUNT; i++){
		a = rand() % ARRAY_LENGTH;
		frequency[a]++;
	}

	for (i = 0; i< ARRAY_LENGTH; i++) {
		printf("Число %d случайное %6d (%5.2f%%) times \n", i, frequency[i],((float)frequency[i] / NUMBERS_AMOUNT * 100));
	}
	EXIT_SUCCESS;
}
