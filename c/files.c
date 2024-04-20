#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *f;
	char c[1000];
	f = fopen("test.odt", "w");
	for(int i = 0; i < 12;i++)
	{
		fprintf(f, "%d\n",i*i);
	}
	fclose(f);

	f = fopen("test.odt","r");
	if (f == NULL)
		printf("fopen Read Error!");
	else

	while (!feof(f))
	{
		if (fscanf(f, "%s", c) > 0)
			printf("%s\n", c);
	}
	fclose(f);

	return 0;
}
