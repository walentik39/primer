#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
	int retcode = execlp("ls", "ls", "-L", "-a", NULL);
	if (retcode == -1)
	{
		perror("execlp");
		return EXIT_FAILURE;
	}
	EXIT_SUCCESS;
}
