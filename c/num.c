#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char* argv[])
{
	int num, rval;
	printf("Введите число [0,9]: ");
	scanf("%d", &num);

	if(num >=0 && num <= 9){
		printf("Это число[0,9]\n");
		rval = 0;
	} else {
		printf("Не то число\n");
		rval = 1;
	}

	return rval;
}

