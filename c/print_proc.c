#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
	pid_t pid = getpid();
	printf("%d\n", pid);
	return 0;
}
