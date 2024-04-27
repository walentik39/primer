#include <stdio.h>
#include <stdlib.h>

int main()
{
	char str[] = "Function fputc() in action.";
	FILE* fp = fopen("my_text.txt","w+");
	for(int i = 0; i < str[i];i++)
	{
		fputc(str[i], fp);
	}
	fclose(fp);

	fp = fopen("my_text.txt","r");
	if (fp == NULL)
		printf("fopen Read Error!");
	else

	while (!feof(fp))
	{
		if (fscanf(fp, "%s", str) > 0)
			printf("%s ", str);
	}
	fclose(fp);

	return 0;
}
