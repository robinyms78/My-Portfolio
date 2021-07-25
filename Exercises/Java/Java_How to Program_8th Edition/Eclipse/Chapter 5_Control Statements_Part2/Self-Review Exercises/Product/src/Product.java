import java.util.Scanner;

public class Product 
{
	public static void main(String arg[]) 
	{
		int integer;
		int product = 1;
	
		for (integer = 1; integer <= 15; integer += 2)
		{
			product *= integer;
		}
		System.out.printf("The product of the odd integers are %d\n ", product);
	}
}

		
