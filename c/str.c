#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int function()
{
	char password[] = "pass";
	char passw[20];
	do
	{
		fprintf(stdout, "введите ваш пароль:\n");
		scanf("%s", passw);
	}while (strcmp(password, passw) !=0); // функция strcmp() сравнивает длинну строк.
	printf("Входите!\n");
	return 0;
}


int main(int argc, char* argv[])
{
	char str[] = "Время всегда хорошее!";
	char sub[] = "всегда";

//работа со строками с помощью strstr(), и strcmp()
	if (strstr(str, sub) == NULL)
	{
		fprintf(stdout, "'%s' не найдено в строке '%s'", sub, str);
	}
	else
	{
		fprintf(stdout, "'%s' было найдено в строке '%s' по адресу %p\n", sub, str, strstr(str, sub));
		fprintf(stdout, "'%s' находится в строке '%s' по индексу %d\n", sub, str, strstr(str, sub) - str);
	}
	function();
	EXIT_SUCCESS;
}
