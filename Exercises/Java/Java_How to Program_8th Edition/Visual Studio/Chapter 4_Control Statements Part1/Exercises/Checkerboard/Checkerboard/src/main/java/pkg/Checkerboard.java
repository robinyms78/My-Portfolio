package pkg;

// Exercise 4.29: Checkerboard.java

public class Checkerboard 
{
	public static void main(String[] args) 
	{
		int size;
		int row;
		int column;

		size = 8;

		column = 1;
		while (column <= size)
		{
			row = 1;
			while (row <= size + 1)
			{
				if (column == 2 || column == 4 || column == 6 || column == 8)
				{
					if (row == 1)
					{
						System.out.print(" ");
					}
					else
					{
						System.out.print("* ");
					}
				}
				else
					if (row == size + 1)
					{
						System.out.print(" ");
					}
				else
				{
					System.out.print("* ");
				}
				row += 1;
			}
			System.out.println();
			column += 1;
		}
	}
}

