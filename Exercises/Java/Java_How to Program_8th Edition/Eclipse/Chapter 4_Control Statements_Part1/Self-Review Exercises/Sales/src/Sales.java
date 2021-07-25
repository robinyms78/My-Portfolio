import java.util.Scanner;

public class Sales 
{
	public void salesCalculator() 
	{
		int item1Counter;
		int item2Counter;
		int item3Counter;
		int item4Counter;
		double item1Value = 239.99;
		double item2Value = 129.75;
		double item3Value = 99.95;
		double item4Value = 350.89;
		double totalSales = 0;
	
		Scanner input = new Scanner(System.in);
	
		System.out.println("Enter the total number of item 1 sold:");
		item1Counter = input.nextInt();
	
		System.out.println("Enter the total number of item 2 sold:");
		item2Counter = input.nextInt();
		
		System.out.println("Enter the total number of item 3 sold:");
		item3Counter = input.nextInt();
		
		System.out.println("Enter the total number of item 4 sold:");
		item4Counter = input.nextInt();
		
		totalSales = 200+ (item1Value * item1Counter + item2Value * item2Counter + item3Value * item3Counter + item4Value + item4Counter) * 0.09; 
		
		System.out.printf("Your total earnings is %.2f\n ", totalSales);
	}
}
