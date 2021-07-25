import java.util.Scanner;

public class Mileage 
{
	public void determineMilesPerGallon()
	{
		Scanner input = new Scanner(System.in);
		
		int miles;
		int gallons;
		int tankCounter;
		int combineMiles;
		int combineGallons;
		double average;
		double averagePerTank;
		
		combineMiles = 0;
		combineGallons = 0;
		tankCounter = 0;
		
		System.out.println("Enter miles driven or -1 to quit: ");
		miles = input.nextInt();
		
		System.out.println("Enter gallons used or -1 to quit: ");
		gallons = input.nextInt();
		
		averagePerTank = (double) miles / gallons;
		System.out.printf("Miles per gallon is %.2f\n", averagePerTank);
		
		while (miles != -1 && gallons != -1)
		{
			combineMiles += miles;
			combineGallons += gallons;
			tankCounter += 1;
			
			System.out.println("Enter miles driven or -1 to quit: ");
			miles = input.nextInt();
			
			System.out.println("Enter gallons used or -1 to quit: ");
			gallons = input.nextInt();
			
			if (miles != -1 && gallons != -1)
			{
				averagePerTank = (double) miles / gallons;
				System.out.printf("Miles per gallon is %.2f\n", averagePerTank);
			}
		}
		
		if (tankCounter != 0)
		{
			average = (double) combineMiles / combineGallons;
			System.out.printf("Combined miles per gallon is %.2f miles/gallon\n", average);
		}	
		else
			System.out.println("No miles and gallons were entered");
	}
}
