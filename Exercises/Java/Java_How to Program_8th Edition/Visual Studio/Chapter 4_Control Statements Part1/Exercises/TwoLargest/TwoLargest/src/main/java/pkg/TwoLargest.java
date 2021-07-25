package pkg;

// Exercise 4.22: TwoLargest

import java.util.Scanner;

public class TwoLargest 
{
	public static void main(String[] args) 
	{
		int counter;
		int firstLargest;
		int secondLargest;
		int number;

		counter = 1;
		firstLargest = 0;
		secondLargest = 0;
		number = 0;
		
		Scanner input = new Scanner(System.in);

		while (counter <= 10)
		{
			System.out.print("Enter the integer: ");
			number = input.nextInt();
			counter += 1;

			if (counter == 1)
			{
				firstLargest = number;
			}
			else 
				if (counter == 2)
				{
					secondLargest = number;
				}
			else
				if (number > firstLargest)
				{
					firstLargest = number;
				}
				if (number > secondLargest)
				{
					if (number < firstLargest)
					{
						secondLargest = number;
					}
				}
		}
		System.out.printf("Two largest integers are %d and %d", firstLargest, secondLargest);
	}
}

