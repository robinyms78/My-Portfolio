package pkg;

// Exercise 4.20: Largest.java

import java.util.Scanner;

public class Largest 
{
	public static void main(String[] args) 
	{
		int counter;
		int largest;
		int number;

		counter = 1;
		number = 0;
		largest = 0;

		Scanner input = new Scanner(System.in);

		while (counter <= 10)
		{
			System.out.print("Enter the integer:");
			number = input.nextInt();
			counter += 1;

			if (counter == 1)
			{
				largest = number;
			}
			else
				if (number > largest)
				{
					largest = number;
				}
		}
		System.out.printf("Largest integer is %d\n", largest);
	}
}
