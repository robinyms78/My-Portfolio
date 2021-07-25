//Fig. 5.5: fig05-05.cpp
//Summing integers with the for statememt

#include <iostream>
using namespace std;

int main()
{
	int total = 0; // initialize total

	// total even integers from 2 through 20
	for (int number = 2; number <= 20; number += 2)
		total += number;

	cout << "Sum is " << total << endl; // display results
} // end main