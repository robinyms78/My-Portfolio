package pkg;

import java.util.Scanner;

public class SmallestLargest2 
{
	public static void main(String[] args) 
	{
		int number1;
		int number2;
		int number3;
		int number4;
		int number5;
		int smallest;
		int largest;

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

	    smallest = number1;
		largest = number1;

		if (number2 < smallest)
			smallest = number2;

		if (number3 < smallest)
			smallest = number3;

		if (number4 < smallest)
			smallest = number4;

		if (number5 < smallest)
			smallest = number5;

	    if (number2 > largest)
			largest = number2;

		if (number3 > largest)
			largest = number3;

		if (number4 > largest)
			largest = number4;

		if (number5 > largest)
			largest = number5;

		System.out.printf("Largest integer is %d\n", largest);
		System.out.printf("Smallest integer is %d ", smallest);
	}
}
