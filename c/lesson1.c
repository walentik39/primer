#include <stdio.h>
#include <stdlib.h>

int global = 100;

int function(void)
{
	puts("function: function");
	int global = 200;
	fprintf(stdout,"global: %i\n",global);
	fprintf(stdout, "local; %i\n", global);
	return 0;
}

int main(void)
{
	puts("function: main");
	int local = 150;
	printf("global: %i\n", global);
	printf("local: %i\n", local);
	function();
	EXIT_SUCCESS;
}
