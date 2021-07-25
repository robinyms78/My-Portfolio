public class Factorial 
{
	public void calculateFactorial()
	{
		int value;
	
		for (value = 1; value <=20; value++)
			System.out.printf("The factorial of %d is %d\n", value, factorial(value));
	}
	
	private long factorial(int integer)
	{
		long factorial = 1;
		int value;
		for (value = 1; value <= integer; value++)
				factorial *= value;
	
		return factorial;
	}
}
