#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
	pid_t pid = getpid();
	pid_t ppid = getppid();
	printf("%d\n%d\n", pid, ppid);
	return 0;
}
