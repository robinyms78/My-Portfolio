// Fig. 3.10: fig03_10.cpp
// Including class GradeBook from file GradeBook.h for use in main
#include <iostream>
#include "GradeBook.h" // include definition of class GradeBook
using namespace std;

// function main begins program execution
int main()
{
	// create two GradeBook objects
	GradeBook gradeBook1("CS101 Introduction to C++ Programming");
	GradeBook gradeBook2("CS102 Data Structure in C++");

	// display initial value of courseName for each GradeBook
	cout << "gradeBook1 created for course: " << gradeBook1.getCourseName()
		 << "\ngradeBook2 created for course: " << gradeBook2.getCourseName() << endl;
} // end main

