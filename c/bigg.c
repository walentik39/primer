#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	time_t biggest = 0x7FFFFFFF;
	printf("biggest = %s \n", ctime(&biggest));

	EXIT_SUCCESS;
}
