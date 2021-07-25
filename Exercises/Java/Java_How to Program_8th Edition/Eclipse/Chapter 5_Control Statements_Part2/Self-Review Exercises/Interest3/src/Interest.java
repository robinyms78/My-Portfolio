public class Interest 
{
	public static void main(String arg[])
	{
		double amount;
		double principal = 1000.0;
		double rate;
		
		System.out.printf("%s%10s%20s\n", "Year", "Rate", "Amount on deposit");
		
		for (rate = 0.05; rate <= 0.10; rate += 0.01)
			for (int year = 1; year <=10; year++)
			{
				amount = principal * Math.pow(1.0 + rate, year);
			
				System.out.printf("%4d%10.2f%,20.2f\n", year, rate, amount);
			}
	}
}
