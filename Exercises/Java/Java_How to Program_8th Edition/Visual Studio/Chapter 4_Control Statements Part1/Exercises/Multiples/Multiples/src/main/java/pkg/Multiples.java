package pkg;

// Exercise 4.30: Multiples.java

public class Multiples 
{
	public static void main(String[] args) 
	{
		int number;
		int counter;

		number = 2;
		counter = 1;

		while (counter > 1)
		{
			System.out.printf("%d\n", number);
			number *= 2;
			counter += 1;
		}
	}
}
