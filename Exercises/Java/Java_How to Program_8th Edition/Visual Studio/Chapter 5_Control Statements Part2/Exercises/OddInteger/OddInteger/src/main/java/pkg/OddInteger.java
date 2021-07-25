// Ex. 5.11: OddInteger.java

package pkg;
import java.util.Scanner;

public class OddInteger 
{
	public static void main(String[] args) 
	{
		int i;
		int product = 1;
		for (i = 1; i <= 15; i+=2)
		{
			product *= i;
		}

		System.out.printf("The product of odd numbers from 1 to 15 is %d", product);
	}
}
