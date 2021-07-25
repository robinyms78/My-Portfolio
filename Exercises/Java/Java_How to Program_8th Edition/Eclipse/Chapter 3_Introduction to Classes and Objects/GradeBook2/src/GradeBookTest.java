import java.util.Scanner;

public class GradeBookTest 
{
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		GradeBook myGradeBook = new GradeBook();
		
		System.out.println("Please enter the course name:");
		String nameOfCourse = input.nextLine();
		System.out.println();
		
		myGradeBook.displayMessage(nameOfCourse);
	}
}
