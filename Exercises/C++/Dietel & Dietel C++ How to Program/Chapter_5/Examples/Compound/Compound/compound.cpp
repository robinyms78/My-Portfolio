// Fig. 5.6: fig 05_06.cpp
// Compound interest calculations with for

#include <iostream>
#include <iomanip>
#include <cmath> // standard C++ math library
using namespace std;

int main()
{
	double amount; // amount on deposit at end of each year
	double principal = 1000.0; // initial amount before interest
	double rate = 0.05; // interest rate

	// display results
	cout << "Year" << setw(21) << "Amount on deposit" << endl;

	// set floating-point number format
	cout << fixed << setprecision(2);

	// calculate amount on deposit for each of ten years
	for (int year = 1; year <= 10; year++)
	{
		// calculate new amount for specified year
		amount = principal * pow(1.0 + rate, year);

		// display the year and the amount
		cout << setw(4) << year << setw(21) << amount << endl;
	} // endl
} // end main

