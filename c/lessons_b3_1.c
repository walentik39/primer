#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	unsigned char flags = 9; // двоичная запись 00001001
	unsigned char mask = 1; // двоичная запись 00000001
	flags = flags ^ mask;	  //исключающая ИЛИ
	printf("flags = %d\n",flags);
	return 0;
}
