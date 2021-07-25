// Ex. 5.16: Sales.java

package pkg;

import java.util.Scanner;

public class Sales 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);

		int number;
		int first = 0;
		int second = 0;
		int third = 0;
		int fourth = 0;
		int fifth = 0;
        int firstCount = 0;
		int secondCount = 0;
		int thirdCount = 0;
		int fourthCount = 0;
		int fifthCount = 0;
		double total;

		System.out.print("Enter the product number (1|2|3|4|5) (-1 to quit): ");
		number = input.nextInt();
		System.out.print("Enter the quantity sold (-1 to quit): ");
		if (number == 1)
			firstCount = input.nextInt();
	    if (number == 2)
			secondCount = input.nextInt();
		if (number == 3)
			thirdCount = input.nextInt();
		if (number == 4)
			fourthCount = input.nextInt();
		if (number == 5)
			fifthCount = input.nextInt();

		while (number != -1)
		{
			System.out.print("Enter the product number (1|2|3|4|5) (-1 to quit): ");
			number = input.nextInt();
			System.out.print("Enter the quantity sold (-1 to quit): ");
			if (number == 1)
				firstCount = input.nextInt();
			if (number == 2)
				secondCount = input.nextInt();
			if (number == 3)
				thirdCount = input.nextInt();
			if (number == 4)
				fourthCount = input.nextInt();
			if (number == 5)
				fifthCount = input.nextInt();

			switch(number)
			{
				case 1:
					first += firstCount;
					break;
				case 2:
					second += secondCount;	
					break;
				case 3:
					third += thirdCount;
					break;
				case 4:
					fourth += fourthCount;
					break;
				case 5:
					fifth += fifthCount;
					break;					
			}
		}

		// Calculate total retal value of all products sold
		total = (firstCount * 2.98) + (secondCount * 4.50) + (thirdCount * 9.98) + (fourthCount * 4.49) + (fifthCount * 6.87);

		// Display results
		System.out.println();
		System.out.printf("The total value is $%.2f", total);
	}
}
