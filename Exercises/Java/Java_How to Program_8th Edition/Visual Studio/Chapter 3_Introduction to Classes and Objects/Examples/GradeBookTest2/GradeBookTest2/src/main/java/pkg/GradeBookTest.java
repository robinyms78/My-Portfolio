package pkg;

// Fig. 3.: GradeBookTest.java
// Create GradeBook object and pass a String to
// its displayMessage method.

import java.util.Scanner; // program uses Scanner

public class GradeBookTest 
{
	// main method begins program execution
	public static void main(String[] args) 
	{
		// create Scanner to obtain input from command window
		Scanner input = new Scanner(System.in);

		// Create a GradeBook object and assigns it to myGradeBook
		GradeBook myGradeBook = new GradeBook();

		// Prompt for and input course name
		System.out.println("Please enter the course name: ");
		String nameOfCourse = input.nextLine(); // read a line of text
		System.out.println();

		// call myGradeBook's displayMessage method
		// and pass nameOfCourse as an argument
		myGradeBook.displayMessage(nameOfCourse);
	} // end main
} // end class GradeBookTest
