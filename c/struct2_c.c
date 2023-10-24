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
	//memset(&st, 0, sizeof(st)); //memset работа с памятью

	printf("st.a = %d, addr: %d\n", st.a, &st.a);
	printf("st.b = %d, addr: %d\n", st.b, &st.b);
	printf("st.c = %d, addr: %d\n", st.c, &st.c);
	printf("sizeof st: %d\n", sizeof(st));
	return 0;
}
