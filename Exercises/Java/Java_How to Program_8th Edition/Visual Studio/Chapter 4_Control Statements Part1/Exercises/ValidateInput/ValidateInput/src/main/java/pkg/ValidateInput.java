package pkg;

// Exercise 4.23: ValidateInput.java

import java.util.Scanner;

public class ValidateInput 
{
	public static void main(String[] args) 
	{
		// create Scanner to obtain input from command window
		Scanner input = new Scanner(System.in);

		// initializing variables in declarations
		int passes = 0; // number of passes
		int failures = 0; // number of failures
		int studentCounter = 1; // student counter
		int result; // one exam result (obtains value from user)

		// process 10 students using counter-controlled loop
		while (studentCounter <= 10)
		{
			// prompt user for input and obtain value from user
			System.out.print("Enter result (1 = pass, 2 = fail): ");
			result = input.nextInt();

			// if .. else nested in while
			if (result == 1)				// if result 1.
			{
				passes = passes + 1;		// increment passes;
				studentCounter = studentCounter + 1;
			}
			
			else
				if (result == 2)				// if result 2,
				{
					failures = failures + 1;	// increment failures
					studentCounter = studentCounter + 1;
				}
			else
				if (result != 1)
				{
					studentCounter = studentCounter;
				}
			else
				if (result != 2)
				{
					studentCounter = studentCounter;
				}
		} // end while

		// termination phase; prepare and display results
		System.out.printf("Passes: %d\nFailed: %d\n", passes, failures);

		// determine whether more than 8 students passed
		if (passes > 8)
			System.out.println("Bonus to instructor!");
	} // end main
} // end class Analysis