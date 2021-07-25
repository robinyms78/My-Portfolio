// This program calculates x raised to the power of y
#include <iostream>
using namespace std;

int main()
{
	int x;
	int y;
	int i = 1; // initialize i to 1
	int power = 1; // initialize power to 1

	cout << "Input x (base): "; // Prompt user to input x (base)
	cin >> x;

	cout << "Input y (exponent): "; // Prompt user to input y (exponent)
	cin >> y;

	while ( i <= y )
	{
		power *= x;
		++i;
	}

	// Print results
	cout << x << " raised to the power of " << y << " is " << power << endl;
}

