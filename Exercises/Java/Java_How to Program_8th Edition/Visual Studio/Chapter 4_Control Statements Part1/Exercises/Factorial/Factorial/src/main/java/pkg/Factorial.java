package pkg;

// Exercise 4.34: Factorial.java 

public class Factorial 
{
	private int number;
	private int startNumber;
	private int factorial;

	// constructor
	public Factorial(int number)
	{
		startNumber = number;
	}

	// calculate factorial
	public void calculateFactorial(int number)
	{
		startNumber = number;
		factorial = number;

		while (number != 1)
		{
			number -=1;
			factorial *= number;
		}
	}

	// return factorial
	public int getFactorial()
	{
		return factorial;
	}

	// display factorial
	public void displayFactorial(int number)
	{
		System.out.printf("Factorial of %d is %d\n", number, getFactorial());
	}
}
