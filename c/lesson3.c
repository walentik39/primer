#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

float foo(float a, float b, float c, float x)
{
	double res;
	res = a*x*x + b*x + c;
	return res;
}
int main()
{
	float y1,y2;
	y1 = foo(1,2,3,0.5);
	y2 = foo(-3.7,5.16, -0.01, 22);
	printf("%f %f\n", y1, y2);
	return 0;
}
