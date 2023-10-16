#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char m = 8;
	char n = 6;
	char s = 4;
	char p = (m > n) ? m : n;//Тернарная оперция
	char x = (m < n) ? m : n;//Если не равно первое неравенство,то выводится последняя переменная
	printf("p = %d\n", p);
	printf("x = %d\n", x);
	EXIT_SUCCESS;
}
