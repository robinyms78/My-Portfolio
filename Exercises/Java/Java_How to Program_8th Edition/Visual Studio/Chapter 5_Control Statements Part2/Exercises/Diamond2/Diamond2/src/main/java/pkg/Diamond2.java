// Ex.5.22: Diamond2.java

package pkg;

import java.util.Scanner;

public class Diamond2 
{
	public static void main(String[] args) 
	{
		int i;
		int j;
		int row;

		Scanner input = new Scanner(System.in);
		System.out.print("Enter an odd number between 1 to 19: ");
		row = input.nextInt();
		
		if (row%2 != 0)
		{
			for (i = 1; i <= row - 4; i++)
			{
				System.out.println();
				// Print first space
				for (j = 1; j <= row - 4 - i; j++)
					System.out.print(" ");
				// Print first triangle
					for (j = 1; j <= i; j++)
					System.out.print("*");
				// Print second triangle
				for (j = 2; j <= i; j++)
					System.out.print("*");
			}	

			for (i = 1; i <= row - 4; i++)
			{
				System.out.println();
				// Print second space
				for (j = 1; j <= i; j++)
					System.out.print(" ");
				// Print third triangle
				for (j = 1; j <= row - 4 - i; j++)
					System.out.print("*");
				// Print fourth triangle
				for (j = 1; j <= row - 5 - i; j++)
					System.out.print("*");
			}
		}
		else
			System.out.print("Invalid number");
	}
}
