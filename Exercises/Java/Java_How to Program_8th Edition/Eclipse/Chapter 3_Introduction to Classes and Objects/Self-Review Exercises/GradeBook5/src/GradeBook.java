public class GradeBook 
{
	private String courseName;
	private String instructorName;
	
	public GradeBook (String name, String nameInstructor)
	{
		courseName = name;
		instructorName = nameInstructor;
	}
	
	public void setCourseName (String name)
	{
		courseName = name;
	}
	
	public String getCourseName()
	{
		return courseName;
	}

	public void setInstructorName (String name)
	{
		instructorName = name;
	}
	
	public String getInstructorName()
	{
		return instructorName;
	}
	
	public void displayMessage()
	{
		System.out.printf("Welcome to the grade book for \n%s!\n", getCourseName());
		System.out.printf("This course is presented by: \n%s!\n", getInstructorName());
	}
}
