#include <stdio.h>
#include <inttypes.h>

int64_t fizz(int64_t);
int64_t buzz(int64_t);

int main(int argc, char* argv[])
{
	for (int i = 1; i < 100; i++)
	{
		if (fizz(i) && buzz(i))
		{
			printf("FizzBuzz\n");
		}
		else if (fizz(i))
		{
			printf("Fizz\n");
		}
		else if (buzz(i))
		{
			printf("Buzz\n");
		}
		else
		{
			printf("%d\n", i);
		}
	}
	return 0;
}
