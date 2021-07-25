import java.util.Scanner;

public class MinimumInteger 
{
	public void determineMinimum()
	{
		int integerTotal;
		int integer;
		int integerCount = 0; 
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("Enter the number of integers: ");
		integerTotal = input.nextInt();
		
		while (integerCount <= integerTotal)
		{
			System.out.print("Enter the integers: ");
			integer = input.nextInt();
			++integerCount;
		
			int result = minimum(integer);		
			System.out.printf("Minimum is %d\n", result);
		}
	}
	
	public int minimum(int x, int y, int z)
	{
		int minimumValue = x;
		
		if (y < minimumValue)
			minimumValue = y;
		
		if (z < minimumValue)
			minimumValue = z;
		
		return minimumValue;
	}
}
