// Fig. 5.18: fig05_18.cpp
// logical operators

#include <iostream>
using namespace std;

int main()
{
	// create truth table for && (logical AND) operator
	cout << boolalpha << "Logical AND (&&)"
		 << "\nfalse && false: " << (false && false)
		 << "\nfalse && true: " << (false && true)
		 << "\ntrue && false: " << (true && false)
		 << "\ntrue && true: " << (true && true) << "\n\n";

	// create truth table for || (logical OR) operator
	cout << boolalpha << "Logical OR (||)"
		 << "\nfalse || false: " << (false || false)
		 << "\nfalse || true: " << (false || true)
		 << "\ntrue || false: " << (true || false)
		 << "\ntrue || true: " << (true || true) << "\n\n";

	// create truth table for ! (logical negation) operator
	cout << boolalpha << "Logical NOT (!)"
		 << "\n!false: " << (!false)
		 << "\n!true: " << (!true) << endl;
} // end main

