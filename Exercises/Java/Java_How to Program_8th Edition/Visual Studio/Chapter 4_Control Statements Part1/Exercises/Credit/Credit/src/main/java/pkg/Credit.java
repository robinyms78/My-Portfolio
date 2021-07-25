package pkg;

// Exercise 4.17: Credit.java

import java.util.Scanner;

public class Credit 
{
	public static void main(String[] args) 
	{
		int account;
		int beginningBalance;
		int newBalance;
		int charges;
		int credits;
		int limit;

		limit = 100;

		Scanner input = new Scanner(System.in);

		System.out.print("Enter account number (-1 to exit): ");
		account = input.nextInt();

		System.out.print("Enter balance (-1 to exit): ");
		beginningBalance = input.nextInt();

		System.out.print("Enter charges (-1 to exit): ");
		charges = input.nextInt();

		System.out.print("Enter credits (-1 to exit): ");
		credits = input.nextInt();

		while (account != -1)
		{
			newBalance = beginningBalance + charges - credits;
			System.out.printf("The new balance is %d\n", newBalance);

			if (newBalance > limit)
			{
				System.out.println("Credit limit exceeded");
			}

			System.out.print("Enter account number (-1 to exit): ");
			account = input.nextInt();

			System.out.print("Enter balance (-1 to exit): ");
			beginningBalance = input.nextInt();

			System.out.print("Enter charges (-1 to exit): ");
			charges = input.nextInt();

			System.out.print("Enter credits (-1 to exit): ");
			credits = input.nextInt();
		}
	}
}
