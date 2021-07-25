// Ex. 5.15: BarChart

package pkg;

import java.util.Scanner;

public class BarChart 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		
		int i;
		int j;
		int number1, number2, number3, number4, number5;
		for (i = 1; i <= 5; i++)
		{
			System.out.print("Enter first number between 1 and 30: ");
			number1 = input.nextInt();

			System.out.print("Enter second number between 1 and 30: ");
			number2 = input.nextInt();

			System.out.print("Enter third number between 1 and 30: ");
			number3 = input.nextInt();

			System.out.print("Enter fourth number between 1 and 30: ");
			number4 = input.nextInt();

			System.out.print("Enter fifth number between 1 and 30: ");
			number5 = input.nextInt();

			// Print first number
			for (j = 1; j <= number1; j++)
			{
				System.out.printf("*");
			}

			// Print second number
			System.out.println();
			for (j = 1; j <= number2; j++)
			{
				System.out.printf("*");
			}

			// Print third number
			System.out.println();
			for (j = 1; j <= number3; j++)
			{
				System.out.printf("*");
			}

			// Print fourth number
			System.out.println();
			for (j = 1; j <= number4; j++)
			{
				System.out.printf("*");
			}

			// Print fifth number
			System.out.println();
			for (j = 1; j <= number5; j++)
			{
				System.out.printf("*");
			}
			break;
		}
	}
}
