package pkg;

// Fig. 3.11: GradeBookTest.java
// GradeBook constructor used to specify the course name at the
// time each GradeBook object is created.

public class GradeBookTest 
{
	// main method begins program execution
	public static void main(String[] args)
	{
	// create GradeBook object
	GradeBook myGradeBook = new GradeBook(
		"CS101 Introduction to Java Programming", "Robin Yap");

	// display the welcome message
	myGradeBook.displayMessage();
	} // end main
} // end class GradeBookTest
