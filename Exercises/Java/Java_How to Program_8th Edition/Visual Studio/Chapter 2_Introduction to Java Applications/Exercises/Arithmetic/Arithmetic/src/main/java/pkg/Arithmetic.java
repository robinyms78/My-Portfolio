package pkg;

import java.util.Scanner;

public class Arithmetic 
{
	public static void main(String[] args) 
	{
		int number1;
		int number2;
		int sum;
		int product;
		int difference;
		int quotient;

		Scanner input = new Scanner(System.in);

		System.out.print("Enter the first integer: ");
		number1 = input.nextInt();

		System.out.print("Enter the second integer: ");
		number2 = input.nextInt();

		sum = number1 + number2;
		product = number1 * number2;
		difference = number1 - number2;
		quotient = number1 / number2;

		System.out.printf("Sum is %d\n", sum);
		System.out.printf("Product is %d\n", product);
		System.out.printf("Difference is %d\n", difference);
		System.out.printf("Quotient is %d\n", quotient);
	}
}
