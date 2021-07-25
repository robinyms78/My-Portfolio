// Exercise 4.12: ex04_12.cpp
#include <iostream>
using namespace std;

int main()
{
	int y; // declare y
	int x = 1; // initialize x
	int total = 0; // initialize total

	while ( x <= 10 ) // loop 10 times
	{
		y = x * x; // perform calculation
		cout << y << endl; // output results
		total += y; // add y to total
		x++; // increment counter x
	} // end while

	cout << "Total is " << total << endl; // display result
} // end main

