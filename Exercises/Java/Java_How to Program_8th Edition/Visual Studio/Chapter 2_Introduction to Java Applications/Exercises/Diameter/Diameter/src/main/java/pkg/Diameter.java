package pkg;

import java.util.Scanner;

public class Diameter 
{
	public static void main(String[] args) 
	{
		int radius;

		Scanner input = new Scanner(System.in);

		System.out.print("Enter the radius: ");
		radius = input.nextInt();

		System.out.printf("Diameter is %d\n", 2 * radius);
		System.out.printf("Circumference is %f\n", 2 * Math.PI * radius);
		System.out.printf("Area is %f\n", Math.PI * radius * radius);
	}
}
