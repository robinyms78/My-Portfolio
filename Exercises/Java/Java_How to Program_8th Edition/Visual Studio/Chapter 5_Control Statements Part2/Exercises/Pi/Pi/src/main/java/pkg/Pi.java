package pkg;

public class Pi 
{
	public static void main(String[] args) 
	{
		int i;
		double result = 0;
		double reciprocal1 = 0;
		double reciprocal2 = 0;
		for (i = 3; i <= 200000; i += 4)
		{
			reciprocal1 += -4/(double)i;
			reciprocal2 += 4/(double)(i+2);
			result = 4 + reciprocal1 + reciprocal2;
		}
		System.out.printf("%d, %.5f\n", i, result);
	}
}
