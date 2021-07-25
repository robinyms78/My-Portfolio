// Ex. 5.20: Trangle2.java

package pkg;

public class Triangle2 
{
	public static void main(String[] args) 
	{
		int row;
		int column;

		// Pattern (a)
		for (row = 1; row <= 10; row++)
		{
			// Print first triangle
			System.out.println();
			for (column = 1; column <= row; column++)
			{
				System.out.print("*");
			}

			// Print first space
			for (column = 1; column <= 11 - row; column++)
			{
				System.out.print(" ");
			}

			// Print second triangle
			for (column = 1; column <= 11 - row; column++)
			{
				System.out.print("*");
			}

			// Print second space
			for (column = 1; column <= row; column++)
			{
				System.out.print(" ");
			}

			// Print third space
			for (column = 1; column <= row; column++)
			{
				System.out.print(" ");
		    }

		    // Print third triangle
			for (column = 1; column <= 11 - row; column++)
			{
				System.out.print("*");
			}

			// Print fourth space
			for (column = 1; column <= 11 - row; column++)
			{
				System.out.print(" ");
			}

		    // Print fourth triangle
			for (column = 1; column <= row; column++)
			{
				System.out.print("*");
			}
		}
	}
}





