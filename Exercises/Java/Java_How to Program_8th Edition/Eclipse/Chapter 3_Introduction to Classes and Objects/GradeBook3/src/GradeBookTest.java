import java.util.Scanner;

public class GradeBookTest 
{

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		
		GradeBook myGradeBook = new GradeBook();
		
		System.out.printf("Initial course name is: %s\n\n", myGradeBook.getCourseName());
		
		System.out.println("Please enter the course name:");
		String theName = input.nextLine();
		myGradeBook.setCourseName(theName);
		System.out.println();
		
		myGradeBook.displayMessage();
	}
}
