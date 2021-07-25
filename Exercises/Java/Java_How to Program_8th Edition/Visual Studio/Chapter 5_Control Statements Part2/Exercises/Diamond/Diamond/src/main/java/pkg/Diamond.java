package pkg;

public class Diamond 
{
	public static void main(String[] args) 
	{
		int i;
		int j;
		for (i = 1; i <= 5; i++)
		{
			System.out.println();
			// Print first space
			for (j = 1; j <= 5 - i; j++)
				System.out.print(" ");
			// Print first triangle
			for (j = 1; j <= i; j++)
				System.out.print("*");
			// Print second triangle
			for (j = 2; j <= i; j++)
				System.out.print("*");
		}

		for (i = 1; i <= 5; i++)
		{
			System.out.println();
			// Print second space
			for (j = 1; j <= i; j++)
				System.out.print(" ");
			// Print third triangle
			for (j = 1; j <= 5 - i; j++)
				System.out.print("*");
			// Print fourth triangle
			for (j = 1; j <= 4 - i; j++)
				System.out.print("*");
		}
	}
}
