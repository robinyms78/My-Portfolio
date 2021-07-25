package pkg;

// Exercise 4.16: Mileage.java

import java.util.Scanner;

public class Mileage 
{
	public static void main(String[] args) 
	{
		int miles;
		int gallons;
		int totalMiles;
		int totalGallons;
		double milesPerGallon;
		double average;

		miles = 0;
		gallons = 0;
		totalMiles = 0;
		totalGallons = 0;

		Scanner input = new Scanner(System.in);

		System.out.print("Enter the miles (-1 to exit): ");
		miles = input.nextInt();		
		
		System.out.print("Enter the gallons (-1 to exit): ");
		gallons = input.nextInt();

		while (miles != -1)
		{
			milesPerGallon = (double) miles / gallons;
			System.out.printf("Miles per gallon is %.2f\n", milesPerGallon);
			
			totalMiles += miles;
			totalGallons += gallons;
			
			System.out.print("Enter the miles (-1 to exit): ");
			miles = input.nextInt();		
		
			System.out.print("Enter the gallons (-1 to exit): ");
			gallons = input.nextInt();		
		}
		 
		 average = (double) totalMiles / totalGallons;
		 System.out.printf("Combined miles per gallon is %.2f", average);
	}
}
