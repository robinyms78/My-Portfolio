package pkg;

// Exercise 4.28: Binary.java

import java.util.Scanner;

public class Binary 
{
	public static void main(String[] args) 
	{
		int number;
		int binary1;
		int binary2;
		int binary3;
		int binary4;
		int binary5;
		int decimal;

		binary1 = 0;
		binary2 = 0;
		binary3 = 0;
		binary4 = 0;
		binary5 = 0; 

		Scanner input = new Scanner(System.in); 

		System.out.print("Enter the number: ");
		number = input.nextInt();
		
		binary1 = number % 10;
		System.out.printf("Binary1 is %d\n", binary1);
		binary2 = (number/10) % 10;
		System.out.printf("Binary2 is %d\n", binary2);
		binary3 = (number/100) % 10;
		System.out.printf("Binary3 is %d\n", binary3);
		binary4 = (number/1000) % 10;
		System.out.printf("Binary4 is %d\n", binary4);
	    binary5 = (number/10000) % 10;
		System.out.printf("Binary5 is %d\n", binary5);

		// Convert binary to decimal
		decimal = binary1 * 1 + binary2 * 2 + binary3 * 4 + binary4 * 8 + binary5 * 16;

		// Print decimal
		System.out.printf("The decimal equivalent of %d is %d\n", number, decimal);
	}
}
