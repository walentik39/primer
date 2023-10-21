#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Test 
{
	char a;
	short b;
	int c;
};

int main(int argc, char* argv[])
{
	struct Test st;
	struct Test * addr = &st;

	addr->a = 5;
	addr->b = 7;
	addr->c = 11;
	//memset(&st, 0, sizeof(st)); //memset работа с памятью

	printf("addr->a = %d\n", addr->a);
	printf("addr->b = %d\n", addr->b);
	printf("addr->c = %d\n", addr->c);
	return 0;
}
