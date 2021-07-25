// Fig. 5.7: fig05_07.cpp
// do ... while repetition statement

#include <iostream>
using namespace std;

int main()
{
	int counter = 1; // initialize counter

	do
	{
		cout << counter << " "; // display counter
		counter++; // increment counter
	} while (counter <= 10); // end do ... while

	cout << endl; // output a newline
} // end main


