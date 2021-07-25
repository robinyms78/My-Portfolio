package pkg;

// Exercise 4.18: Sales.java

import java.util.Scanner;

public class Sales 
{
	public static void main(String[] args) 
	{
		int item1;
		int item2;
		int item3;
		int item4;
		double earnings;

		Scanner input = new Scanner(System.in);

		System.out.print("Enter number of item 1 sold (-1 to exit): ");
		item1 = input.nextInt();

		System.out.print("Enter number of item 2 sold (-1 to exit): ");
		item2 = input.nextInt();
		
		System.out.print("Enter number of item 3 sold (-1 to exit): ");
		item3 = input.nextInt();
		
		System.out.print("Enter number of item 4 sold (-1 to exit): ");
		item4 = input.nextInt();

		while (item1 != -1)
		{
			earnings = 200 + 0.09 * (item1 * 239.99) +
							 0.09 * (item2 * 129.75) +
							 0.09 * (item3 * 99.95) +
							 0.09 * (item4 * 350.89);
			System.out.printf("Salesperson's earnings is $%.2f\n", earnings);
			
			System.out.print("Enter number of item 1 sold (-1 to exit): ");
			item1 = input.nextInt();
			
			System.out.print("Enter number of item 2 sold (-1 to exit): ");
			item2 = input.nextInt();
			
			System.out.print("Enter number of item 3 sold (-1 to exit): ");
			item3 = input.nextInt();
			
			System.out.print("Enter number of item 4 sold (-1 to exit): ");
			item4 = input.nextInt();
		}
	}
}
