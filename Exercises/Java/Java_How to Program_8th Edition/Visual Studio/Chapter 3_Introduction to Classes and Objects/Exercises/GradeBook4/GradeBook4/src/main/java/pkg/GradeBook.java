package pkg;

// Fig. 3.10: GradeBook.java
// GradeBook class with a constructor to initialize the course name.

public class GradeBook 
{
	private String courseName; // course name for this GradeBook
	private String instructorName; // instructor name for this GradeBook

	// constructor initializes courseName and instructorName with String argument
	public GradeBook(String nameOfCourse, String nameOfInstructor) 
	{
		courseName = nameOfCourse; // initializes courseName
		instructorName = nameOfInstructor; // initializes instructorName
	} // end constructor

	// method to set the course name
	public void setCourseName(String nameOfCourse)
	{
		courseName = nameOfCourse; // store the course name
	} // end method setCourseName

	// method to set the instructor name
	public void setInstructorName(String nameOfInstructor)
	{
		courseName = nameOfInstructor; // store the instructor name
	} // end method setInstructorName

	// method to retrieve the course name
	public String getCourseName()
	{
		return courseName;
	} // end method getCourseName

    // method to retrieve the instructor name
	public String getInstructorName()
	{
		return instructorName;
	} // end method getInstructorName

	// display a welcome message to the GradeBook user
	public void displayMessage()
	{
		// this statement calls getCourseName to get the
		// name of the course this GradeBook represents
		System.out.printf("Welcome to the grade book for \n%s!\n",
				getCourseName());
		System.out.printf("This course is presented by: %s\n",
				getInstructorName());
	} // end method displayMessage
} // end class GradeBook

