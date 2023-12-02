#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
	char *args[] = {"ls","-l","-a",NULL};
	int retcode = execvp(args[0], args);
	if (retcode == -1)
	{
		perror("execlp");
		return EXIT_FAILURE;
	}
	return EXIT_SUCCESS;
}
