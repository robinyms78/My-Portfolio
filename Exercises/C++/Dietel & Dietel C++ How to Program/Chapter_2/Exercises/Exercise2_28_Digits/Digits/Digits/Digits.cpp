// Digits.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
    int number;
    int digit1;
    int digit2;
    int digit3;
    int digit4;
    int digit5;
    cout << "Enter a five-digit integer: ";
    cin >> number;

    digit1 = number / 10000;
    digit2 = (number / 1000) % 10;
    digit3 = (number / 100) % 100 % 10;
    digit4 = (number / 10) % 1000 % 100 % 10;
    digit5 = number % 10000 % 1000 % 100 % 10;

    cout << digit1 << "   " << digit2 << "   " << digit3 << "   " << digit4 << "   " << digit5 << endl;
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
