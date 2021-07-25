package pkg;

// Exercise 4.33: RightTriangle.java

import java.util.Scanner;

public class RightTriangle 
{
	public static void main(String[] args) 
	{
		int side1;
		int side2;
		int side3;

		Scanner input = new Scanner(System.in);

		System.out.print("Enter the first side: ");
		side1 = input.nextInt();

		System.out.print("Enter the second side: ");
		side2 = input.nextInt();

		System.out.print("Enter the third side: ");
		side3 = input.nextInt();

		if (side1 * side1 + side2 * side2 == side3 * side3)
		{
			System.out.print("The sides could represent the sides of a right triangle");
		}
		else
			if (side1 * side1 + side3 * side3 == side2 * side2)
			{
				System.out.print("The sides could represent the sides of a right triangle");
			}
		else
			if (side2 * side2 + side3 * side3 == side1 * side1)
			{
			System.out.print("The sides could represent the sides of a triangle");
			}
		else
			System.out.print("The sides could not represent the sides of a right triangle");
	}
}
