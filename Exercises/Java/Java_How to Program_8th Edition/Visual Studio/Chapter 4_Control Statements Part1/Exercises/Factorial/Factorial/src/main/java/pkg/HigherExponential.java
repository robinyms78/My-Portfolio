package pkg;

// Exercise 4.34: HigherExponential.java

import java.util.Scanner;

public class HigherExponential 
{
	private double exponential;
	private int terms;
    private int number;
	private int startNumber;
	private int factorial;
	private int x;

	// constructor
	public HigherExponential(int number, int number2)
	{
		terms = number;
		x = number2;
	}

	// calculate factorial
	public int getFactorial(int number)
	{
		startNumber = number;
		factorial = number;

		while (number != 1)
		{
			number -=1;
			factorial *= number;
		}
		return factorial;
	}

	// calculate exponential
	public void calculateExponential(int number, int number2)
	{
		int counter;
		double reciprocal;

		counter = 1;
		reciprocal = 0;

		Scanner input = new Scanner(System.in);

		while (counter < number)
		{
		    reciprocal += (double) Math.pow(number2, counter) / getFactorial(counter);
			exponential = 1 + reciprocal;
			counter += 1;
		}
	}

	// get exponential
	public double getExponential()
	{
		return exponential;
	}

	// display exponential
	public void displayExponential(int number, int number2)
	{
		System.out.printf("The exponential containing %d terms with x equal to %d is %.2f\n", number, number2, getExponential());
	}
}
