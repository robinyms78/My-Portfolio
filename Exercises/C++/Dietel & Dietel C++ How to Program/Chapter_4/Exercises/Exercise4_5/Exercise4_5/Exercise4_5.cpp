// This program adds the integer from 1 to 10
#include <iostream>
using namespace std;

int main()
{
	int x;
	int sum;

	x = 1;	// Initialize x to 1
	sum = 0; // Initialize sum to 0

	while ( x <= 10)
	{
		sum += x; // add x to sum
		x += 1;   // increment x by 1
	} // end while loop

	// Print sum
	cout << "The sum is : " << sum << endl;
} // end function main

