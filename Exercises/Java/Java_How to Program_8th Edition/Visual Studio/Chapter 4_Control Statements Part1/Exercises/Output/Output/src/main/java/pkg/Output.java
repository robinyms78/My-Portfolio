package pkg;

// Exercise 4.21: Output.java

public class Output 
{
	public static void main(String[] args) 
	{
		int N;
		int counter;

		N = 1;
		counter = 1;
		
		System.out.println("N     10*N     100*N     1000*N");
		System.out.println();

		while (counter <= 5)
		{
			System.out.printf("%d     %d       %d       %d\n", N, 10*N, 100*N, 1000*N);
			counter += 1;
			N += 1;
		}
	}
}
