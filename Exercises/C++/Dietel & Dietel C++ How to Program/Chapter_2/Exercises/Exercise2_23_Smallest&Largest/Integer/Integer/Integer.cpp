// Integer.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

int main()
{
    int number1;
    int number2;
    int number3;
    int number4;
    int number5;
    int min, max;
    cout << "Enter 5 integers: \n";
    cin >> number1 >> number2 >> number3 >> number4 >> number5;

    min = number1;
    if (number2 < number1)
        min = number2;
    if (number3 < number2)
        min = number3;
    if (number4 < number3)
        min = number4;
    if (number5 < number4)
        min = number5;

    max = number1;
    if (number2 > number1)
        max = number2;
    if (number3 > number2)
        max = number3;
    if (number4 > number3)
        max = number4;
    if (number5 > number4)
        max = number5;

    cout << "Largest integer is " << max << endl;
    cout << "Smallest integer is " << min << endl;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
