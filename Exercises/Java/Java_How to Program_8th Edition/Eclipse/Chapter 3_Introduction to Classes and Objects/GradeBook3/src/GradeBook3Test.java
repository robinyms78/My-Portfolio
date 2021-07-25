// Creating and manipulating a GradeBook object
import java.util.Scanner;

public class GradeBook3Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Create scanner to obtain new input from command window
		Scanner input = new Scanner(System.in);
		
		// Create a GradeBook object and assign it to myGradeBook
		GradeBook3 myGradeBook = new GradeBook3();
		
		// Display initial value of courseName
		System.out.printf("Initial course name is: %s\n\n", myGradeBook.getCourseName());
		
		// Prompt for and read course name
		System.out.println("Please enter the course name: ");
		String theName = input.nextLine(); // read a line of text
		myGradeBook.setCourseName(theName); // set the course name
		System.out.println(); // outputs a blank line
		
		// Display welcome message after specifying course name
		myGradeBook.displayMessage();
	}
}
