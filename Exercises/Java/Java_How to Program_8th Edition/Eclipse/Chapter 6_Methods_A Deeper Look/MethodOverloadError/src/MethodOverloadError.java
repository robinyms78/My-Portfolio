public class MethodOverloadError 
{
	public void methodOverload() 
	{
		System.out.printf("The suqare of 5 is %d\n", square(5));
		System.out.printf("The square of 5.5 is %f\n", square(5.5));
	}
	
	public int square(int x)
	{
		return x * x;
	}
	
	public double square(double y)
	{
		return y * y;
	}
	
}
