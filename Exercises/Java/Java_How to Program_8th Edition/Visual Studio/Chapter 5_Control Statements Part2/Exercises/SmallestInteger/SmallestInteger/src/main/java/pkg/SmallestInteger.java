// Ex. 5.10: SmallestInteger.java

package pkg;

import java.util.Scanner;

public class SmallestInteger 
{
	public static void main(String[] args) 
	{
		int number;
		int total;
		int smallest = 10000; // Initialize smallest number to a large integer

		Scanner input = new Scanner(System.in);

		System.out.print("Enter the number of integers: ");
		total = input.nextInt();
		
		int count = 1;
		while (count <= total)
		{
			Scanner input2 = new Scanner(System.in); 
			System.out.printf("Enter the integer:");
			number = input.nextInt(); 
			count++;

			if (count == 1)
			{
				smallest = number;
			}
			else
				if (number < smallest)
				{
					smallest = number;
				}
		}
		System.out.printf("The smallest integer is %d", smallest);
	}
}
