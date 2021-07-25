package pkg;

// Exercise 4.27: Palindromes.java

import java.util.Scanner;

public class Palindromes 
{
	public static void main(String[] args) 
	{
		int number1;
		int number2;
		int number3;
		int number4;
		int number5;
		int number;

		number1 = 0;
		number2 = 0;
		number3 = 0;
		number4 = 0;
		number5 = 0;

		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter the number: ");
		number = input.nextInt();

		while (number / 1000 < 10)
		{
			System.out.print("Number is not five digit long. Please enter the number again: ");
			number = input.nextInt();
		}

		// Determine the respective digits
		number1 = number / 10000;
		System.out.printf("Number1 is %d\n", number1);
		number2 = number / 1000 - number1 * 10;
		System.out.printf("Number2 is %d\n", number2);
		number3 = number / 100 - number1 * 100 - number2 * 10;
		System.out.printf("Number3 is %d\n", number3);
		number4 = number / 10 - number1 * 1000 - number2 * 100 - number3 * 10;
		System.out.printf("Number4 is %d\n", number4);
		number5 = number - number1 * 10000 - number2 * 1000 - number3 * 100 - number4 * 10;
		System.out.printf("Number5 is %d\n", number5);

		// Check for palindromes
		if (number1 == number5)
		{
			if (number2 == number4)
			{
				System.out.printf("The integer %d is a palindrome", number);
			}  
		}
		else
			System.out.printf("The integer %d is not a palindrome", number);
	}
}

