// Fig. 5.13: fig05_13.cpp
// break statement exiting a for statement

#include <iostream>
using namespace std;

int main()
{
	int count; // control variable also used after loop terminates
	for (count = 1; count <= 10; count++) // loop 10 times
	{
		if (count == 5)
			break; // break loop only if x is 5
		cout << count << " ";
	} // end for

	cout << "\nBroke out of loop at count = " << count << endl;
} // end main


