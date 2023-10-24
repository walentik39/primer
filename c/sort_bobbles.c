#include <stdio.h>
#include <stdlib.h>
#define ARRAY_LENGTH 50

int main(int argc, const char* argv[])
{
	int array[5] = {2, 3, 8, 21, 5};
	for(int i=0;i<5;i++){
		for(int j = 0; j< 5 -i -1;j++){
			if(array[j] > array[j+1]){
				int tmp = array[j];
				array[j] = array[j+1];
				array[j+1] = tmp;
				printf("%d\n", array[j+1]);
			}
		}
	}


	return 0;
}


					

