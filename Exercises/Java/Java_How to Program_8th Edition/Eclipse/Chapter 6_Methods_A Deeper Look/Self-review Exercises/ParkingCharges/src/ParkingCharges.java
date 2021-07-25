import java.util.Scanner;

public class ParkingCharges
{
	int hours;
	double charges;
	double minimum = 2.00;
	double maximum = 10.00;
	int customerCounter = 0;
	double total = 0;
	
	public void calculateCharges()
	{
		Scanner input = new Scanner(System.in);
		
		while (hours != -1)
		{
			total += charges;
			++customerCounter;
			
			System.out.println("Enter the number of hours parked or -1 to quit: \n");
			hours = input.nextInt();
			
			if (hours < 3)
				charges = minimum;
			else
				charges = minimum + 0.5 * (hours - 3);  
		
			if (charges > maximum)
				charges = maximum;
		
			System.out.printf("Total parking charges for customer is $%.2f\n", charges);
			
		}
		
		if (customerCounter !=0)
		{
			System.out.printf("Total parking charges for all customers is $%.2f\n", total);
		}
	}
}
