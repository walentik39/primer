#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Test 
{
	int a;
	int b;
	int c;
};

int main(int argc, char* argv[])
{
	struct Test st;

	st.a = 5;
	st.b = 7;
	st.c = 11;

	printf("st.a = %d, addr: %d\n", st.a, &st.a);
	printf("st.b = %d, addr: %d\n", st.b, &st.b);
	printf("st.c = %d, addr: %d\n", st.c, &st.c);
	return 0;
}
