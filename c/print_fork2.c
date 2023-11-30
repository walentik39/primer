#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(int argc, char* argv[])
{
	pid_t pid = fork();
	if (!pid)
	{
		printf("Hello from child process!\n");
		exit(EXIT_SUCCESS);
	}
	else if (pid == -1)
	{
		perror("fork");
		exit(EXIT_FAILURE);
	}
	pid = wait(NULL);
	if (pid == -1)
	{
		perror("wait");
		exit(EXIT_FAILURE);
	}
	return 0;
}
