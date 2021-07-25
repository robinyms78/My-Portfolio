package pkg;

import java.util.Scanner;

public class NegativePositive 
{
	public static void main(String[] args) 
	{
		int number1;
		int number2;
		int number3;
		int number4;
		int number5;
		int countNegative = 0;
		int countPositive = 0;
		int countZero = 0;

		Scanner input = new Scanner(System.in);

		System.out.print("Enter first integer: ");
		number1 = input.nextInt();

	    System.out.print("Enter second integer: ");
		number2 = input.nextInt();

		System.out.print("Enter third integer: ");
		number3 = input.nextInt();

	    System.out.print("Enter fourth integer: ");
		number4 = input.nextInt();

		System.out.print("Enter fifth integer: ");
		number5 = input.nextInt();

		if (number1 > 0)
			countPositive = countPositive + 1;

	    if (number1 < 0)
			countNegative = countNegative + 1;

	    if (number1 == 0)
			countZero = countZero + 1;

	    if (number2 > 0)
			countPositive = countPositive + 1;

	    if (number2 < 0)
			countNegative = countNegative + 1;

	    if (number2 == 0)
			countZero = countZero + 1;

	    if (number3 > 0)
			countPositive = countPositive + 1;

	    if (number3 < 0)
			countNegative = countNegative + 1;

	    if (number3 == 0)
			countZero = countZero + 1;

		if (number4 > 0)
			countPositive = countPositive + 1;

	    if (number4 < 0)
			countNegative = countNegative + 1;

	    if (number4 == 0)
			countZero = countZero + 1;

	    if (number5 > 0)
			countPositive = countPositive + 1;

	    if (number5 < 0)
			countNegative = countNegative + 1;

	    if (number5 == 0)
			countZero = countZero + 1;

		System.out.printf("Number of negative numbers input is %d\n", countNegative);
		System.out.printf("Number of positive numbers input is %d\n", countPositive);
		System.out.printf("Number of zeros input is %d\n", countZero);
	}
}
