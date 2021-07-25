import java.util.Scanner;

public class Exponentiation 
{
	public void exponential()
	{
		int base;
		int exponent;
		int result = 1;
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("Please enter the base: ");
		base = input.nextInt();
		
		System.out.println("Please enter the exponent: ");
		exponent = input.nextInt();
		
		for (int value = 1; value <= exponent; ++value)
			result *= base;
		
		System.out.printf("The result is %d\n", result);
	}
}
