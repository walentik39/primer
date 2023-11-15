#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int checkPass(char *pass)
{
	int result_flag = 0;
	char password_buffer[16];

	strcpy(password_buffer, pass);
	if (strcmp(password_buffer, "some_pass") == 0)
	{
		result_flag = 1;
	}
	return result_flag;
}

int main(int argc, char* argv[])
{
	if (checkPass(argv[1]))
	{
		printf("Granted\n");
	}
	else
	{
		printf("Denied\n");
	}
}
