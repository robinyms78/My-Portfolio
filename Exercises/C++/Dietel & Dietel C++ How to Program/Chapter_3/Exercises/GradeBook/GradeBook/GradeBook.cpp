// This program contains the member function implementation for class GradeBook
#include <iostream>
#include "GradeBook.h"
using namespace std;

// Constructor for GradeBook
GradeBook::GradeBook( string nameOfCourse, string nameOfInstructor)
{
	setCourseName( nameOfCourse );
	setInstructorName ( nameOfInstructor );
}

// Set course name for GradeBook
void GradeBook::setCourseName( string nameOfCourse )
{
	courseName = nameOfCourse;
}

// Set instructor name for GradeBook
void GradeBook::setInstructorName ( string nameOfInstructor )
{
	instructorName = nameOfInstructor;
}

// Get course name for GradeBook
string GradeBook::getCourseName()
{
	return courseName;
}

// Get instructor name for GradeBook
string GradeBook::getInstructorName()
{
	return instructorName;
}

// Display course name and instructor name
void GradeBook::displayMessage()
{
	cout << "Welcome to the grade book for\n" << getCourseName()
		 << "\nThis course is presented by: " << getInstructorName() << "!" << endl;
}











