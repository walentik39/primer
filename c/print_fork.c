#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
	pid_t pid = fork();
	if (pid > 0)
	{
		printf("Parent process pid: %d\n", getpid());
	}
	else if (pid == 0)
	{
		printf("Child process pid: %d\n", getpid());
		printf("parent process pid: %d\n", getppid());
	}
	else
	{
		perror("fork");
	}
	return 0;
}
