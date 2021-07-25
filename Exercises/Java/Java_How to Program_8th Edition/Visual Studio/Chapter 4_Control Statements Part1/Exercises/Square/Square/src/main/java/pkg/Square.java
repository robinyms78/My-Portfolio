package pkg;

// Exercise 4.26: Square.java

import java.util.Scanner;

public class Square 
{
	public static void main(String[] args) 
	{
		int size;
		int row;
		int column;

		size = 0;
		row = 1;
		column = 1;

		Scanner input = new Scanner(System.in);

		System.out.print("Enter the size of the sides of the square: ");
		size = input.nextInt();

		// Print first row
		while (row <= size)
		{
			System.out.print("*");
			row += 1;
		}
		System.out.print("\n");

		// Print column
		while (column <= size - 2)
		{
			row = 1;
			while (row <= size)
			{
				if (row == 1||row == size)
				{
					System.out.print("*");
					}
				else
				{
					System.out.print(" ");
					}
			row +=1;
			}
		System.out.print("\n");
		column += 1;
		}
		
		// Print last row
		row = 1;
		while (row <= size)
		{
			System.out.print("*");
			row += 1;
		}
		System.out.print("\n");
	}
}
