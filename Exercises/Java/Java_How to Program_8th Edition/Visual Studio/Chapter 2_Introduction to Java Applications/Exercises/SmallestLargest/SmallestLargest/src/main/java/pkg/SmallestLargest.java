package pkg;

import java.util.Scanner;

public class SmallestLargest 
{
	public static void main(String[] args) 
	{
		int number1;
		int number2;
		int number3;
		int sum;
		int average;
		int product;
		int largest;
		int smallest;

		Scanner input = new Scanner(System.in);

		System.out.print("Enter first integer: ");
		number1 = input.nextInt();

		System.out.print("Enter second integer: ");
		number2 = input.nextInt();

		System.out.print("Enter third integer: ");
		number3 = input.nextInt();

		sum = number1 + number2 + number3;
		average = (number1 + number2 + number3) / 3;
		product = number1 * number2 * number3;

		System.out.printf("Sum is %d\n", sum);
		System.out.printf("Average is %d\n", average);
		System.out.printf("Product is %d\n", product);

		largest = number1; // assume number1 is the largest to start with
		smallest = number1; // assume number1 is the smallest to start with

		if (number2 > largest) 
			largest = number2;

		if (number3 > largest) 
			largest = number3;

		if (number2 < smallest)
			smallest = number2;

		if (number3 < smallest)
			smallest = number3;

		System.out.printf("Smallest number is %d\n", smallest);
		System.out.printf("Largest number is %d\n", largest);
	}
}
