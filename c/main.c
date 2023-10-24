#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__attribute__((constructor)) void f1()
{
	printf("function f1\n");
}

__attribute__((destructor)) void f2()
{
	printf("funtion f2\n");
}
int main(int argc, char* argv[])
{
	printf("main start\n");

	printf("main ends\n");
	EXIT_SUCCESS;
}
