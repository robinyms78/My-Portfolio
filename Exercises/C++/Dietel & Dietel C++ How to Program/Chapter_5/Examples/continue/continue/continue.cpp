// Fig. 5.14: fig 05_14.cpp
// continue statement terminating an iteration of a for statement

#include <iostream>
using namespace std;

int main()
{
	for (int count = 1; count <= 10; count++) // loop 10 times
	{
		if (count == 5) // if count is 5, skip remaining code in loop
			continue;
		cout << count << " ";
	} // end for

	cout << "\nUsed continue to skip printing 5" << endl;
} // end main

