package pkg;

// Exercise 4.34: FactorialTest.java 

import java.util.Scanner;

public class FactorialTest 
{
	public static void main(String[] args)
	{
		// create instance of the respective classes and initialize argument to 0
		Factorial factorial = new Factorial(0);
		Exponential exponential = new Exponential(0);
		HigherExponential higherExponential = new HigherExponential(0, 0);
		Scanner input = new Scanner(System.in);

		// obtain input from command window (Factorial)
		int number;
		System.out.print("Enter the integer for factorial: ");
		number = input.nextInt();

		// obtain input from command window (Exponential)
		int terms;
		System.out.print("Enter the number of terms for exponential: ");
		terms = input.nextInt();

		// obtain input from command window (Higher Exponential)
		int terms2;
		int x;
		System.out.print("Enter the number of terms for higher exponential: ");
		terms2 = input.nextInt();

		System.out.print("Enter the value of x for higher exponential: ");
		x = input.nextInt();

		// calculate factorial
		factorial.calculateFactorial(number);
		
		// display factorial
		factorial.displayFactorial(number);

		// calculate exponential
		exponential.calculateExponential(terms);

		// display exponential
		exponential.displayExponential(terms);

		// calculate higher exponential
		higherExponential.calculateExponential(terms2, x);

		// display higher exponential
		higherExponential.displayExponential(terms2, x);
	}
}