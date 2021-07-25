// Create GradeBook object and pass a string to its displayMessage method
import java.util.Scanner;

public class GradeBook2Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		
		GradeBook2 myGradeBook = new GradeBook2();
		
		System.out.println("Please enter the course name: ");
		String nameOfCourse = input.nextLine();
		System.out.println();
		
		myGradeBook.displayMessage(nameOfCourse);
	}
}
