package pkg;

// Exercise 4.19: Salary.java

import java.util.Scanner;

public class Salary 
{
	public static void main(String[] args) 
	{
		int employee;
		int hours;
		int rate;
		int pay;
		int counter;

		counter = 1;

		Scanner input = new Scanner(System.in);

		while (counter <= 3)
		{
			System.out.print("Enter the employee number(1 | 2 | 3):");
			employee = input.nextInt();

			System.out.print("Enter the employee's number of hours worked:");
			hours = input.nextInt();

			System.out.print("Enter the employee's hourly rate:");
			rate = input.nextInt();
			counter += 1;

			if (hours <= 40)
			{
				pay = 40 * rate;
				System.out.printf("Employee %d's gross pay is %d\n", employee, pay);
			}
			else
			{
				pay = hours * rate + (hours - 40) * rate / 2;
				System.out.printf("Employee %d's gross pay is %d\n", employee, pay);
			}
		}
	}
}
