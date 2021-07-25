// arithmetic.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

int main()
{
    int number1;
    int number2;
    int sum;
    int product;
    int difference;
    int quotient;

    cout << "Enter the first integer: ";
    cin >> number1;

    cout << "Enter the second integer: ";
    cin >> number2;

    sum = number1 + number2;
    difference = number1 - number2;
    product = number1 * number2;
    quotient = number1 / number2;

    cout << "The sum of " << number1 << " and " << number2 << " is " << sum << endl;
    cout << "The difference of " << number1 << " and " << number2 << " is " << difference << endl;
    cout << "The product of " << number1 << " and " << number2 << " is " << product << endl;
    cout << "The quotient of " << number1 << " and " << number2 << " is " << quotient << endl;

}
