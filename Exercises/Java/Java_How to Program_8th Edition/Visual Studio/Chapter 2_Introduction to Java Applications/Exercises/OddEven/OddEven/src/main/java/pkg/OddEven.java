package pkg;

import java.util.Scanner;

public class OddEven 
{
	public static void main(String[] args) 
	{
		int number1;

		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter integer: ");
		number1 = input.nextInt();

		if (number1 % 2 == 0)
			System.out.print("Number is even");
		
		if (number1 % 2 != 0)
			System.out.print("Number is odd");	
	}
}
