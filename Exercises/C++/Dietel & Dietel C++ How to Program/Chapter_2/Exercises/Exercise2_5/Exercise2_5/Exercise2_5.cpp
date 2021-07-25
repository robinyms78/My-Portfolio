// This program calculates the product of three integers

#include <iostream>
using namespace std;

int main()
{
	int number1; // Integer 1
	int number2; // Integer 2
	int number3; // Integer 3
	int result;  // Product 

	cout << "Enter three integers: ";		// Prompt user to input three integers
	cin >> number1 >> number2 >> number3;	// Read integer input from user
	result = number1 * number2 * number3;   // Calculate product of three integers
	cout << "The product is " << result << endl;	// Display result

	return 0;
}

