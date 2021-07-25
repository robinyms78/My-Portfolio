package pkg;

// Exercise 4.34: Exponential.java

import java.util.Scanner;

public class Exponential 
{
	private double exponential;
	private int terms;
    private int number;
	private int startNumber;
	private int factorial;

	// constructor
	public Exponential(int number)
	{
		terms = number;
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
	public void calculateExponential(int number)
	{
		int counter;
		double reciprocal;

		counter = 1;
		reciprocal = 0;

		Scanner input = new Scanner(System.in);

		while (counter < number)
		{
		    reciprocal += (double) 1 / getFactorial(counter);
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
	public void displayExponential(int number)
	{
		System.out.printf("The exponential containing %d terms is %.2f\n", number, getExponential());
	}
}
