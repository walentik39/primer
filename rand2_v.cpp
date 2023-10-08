#include <iostream>
#include <ctime>

using namespace std;
int main()
{

	srand(time(NULL));
	for (int i=0; i <6; i++)
		for (int j=i+1;j<rand()%12;j++)
		{
		int a = rand()%10;
		cout << a << endl;
		int b = rand()%100;
		cout << b << endl;
		}
}
