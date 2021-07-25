// BMI.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
    int weight;
    float height;
    float BMI;

    cout << "Enter your weight in kg: ";
    cin >> weight;
    cout << "Enter your height in m: ";
    cin >> height;

    BMI = weight / (height * height);
    cout << "Your BMI is : " << BMI << endl;
    cout << "BMI VALUES\n";
    cout << "Underweight:" << "\t" << "less than 18.5\n";
    cout << "Normal:" << "\t\t" << "between 18.5 and 24.9\n";
    cout << "Overweight:" << "\t" << "between 25 and 29.9\n";
    cout << "Obese:" << "\t\t" << "30 or greater\n";
}

