#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	unsigned char flags = 5; // двоичная запись 00000101
	unsigned char mask = 4; // результат 01100100
	unsigned char res = flags & mask;			  
	printf("res = %d\n",res);
	return 0;
}
