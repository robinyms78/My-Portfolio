package pkg;

public class Triangle 
{
	public static void main(String[] args) 
	{
		int row;
		int column;

		// Pattern (a)
		for (row = 1; row <= 10; row++)
		{
			System.out.println();
			for (column = 1; column <= row; column++)
			{
				System.out.print("*");
			}
		}

		// Pattern (b)
		System.out.println();
		for (row = 1; row <= 10; row++)
		{
			System.out.println();
			for (column = 1; column <= 11 - row; column++)
			{
				System.out.print("*");
			}
		}

	    // Pattern (c)
		System.out.println();
		for (row = 1; row <= 10; row++)
		{
			System.out.println();
			// Print spaces
			for (column = 1; column <= row - 1; column++)
			{
				System.out.print(" ");
			}

		    // Print asterisks
			for (column = 1; column <= 11 - row; column++)
			{
				System.out.print("*");
			}
		}

	    // Pattern (d)
		System.out.println();
		for (row = 1; row <= 10; row++)
		{
			System.out.println();
			// Print spaces
			for (column = 1; column <= 11 - row; column++)
			{
				System.out.print(" ");
			}

		    // Print asterisks
			for (column = 1; column <= row; column++)
			{
				System.out.print("*");
			}
		}
	}
}




