// SmallestLargest.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
    int number1;
    int number2;
    int number3;
    int sum;
    int average;
    int product;

    cout << "Enter three different integers: ";
    cin >> number1 >> number2 >> number3;

    sum = number1 + number2 + number3;
    cout << "Sum is " << sum << endl;
    
    average = (number1 + number2 + number3) / 3;
    cout << "Average is " << average << endl;
    
    product = number1 * number2 * number3;
    cout << "Product is " << product << endl;

    int min = number1;
    if (min > number2)
        min = number2;
    if (min > number3)
        min = number3;
    cout << "Smallest is " << min << endl;

    int max = number1;
    if (max < number2) 
        max = number2;
    if (max < number3) 
        max = number3;
    cout << "Largest is " << max << endl;

    system("pause");
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
