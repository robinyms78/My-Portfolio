package pkg;

// Fig. 5.5: Sum
// Summing integers with the for statement.

public class Sum 
{
	public static void main(String[] args) 
	{
		int total = 0; // initialize total

		// total even integers from 2 through 20
		for (int number = 2; number <= 20; number += 2)
			total += number;

		System.out.printf("Sum is %d\n", total); // display results
	} // end main
} // end class Sum
