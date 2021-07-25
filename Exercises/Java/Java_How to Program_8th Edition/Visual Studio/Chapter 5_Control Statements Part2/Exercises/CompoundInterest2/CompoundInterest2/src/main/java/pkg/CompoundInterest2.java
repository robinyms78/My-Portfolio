package pkg;

public class CompoundInterest2 
{
	public static void main(String[] args) 
	{
		int amount; // amount on deposit at end of each year
		int principal = 100000; // initial amount before interest
		int rate = 5; // interest rate
		int dollar;
		int cent;
		
		// display headers
		System.out.printf("%s%20s\n", "Year", "Amount on deposit");

		// calculate amount on deposit for each of ten years
		for (int year = 1; year <= 10; year++)
		{
			// calculate new amount for specified year
			amount = principal * (int)Math.pow(100 + rate, year) / (int)Math.pow(100, year) ;
			dollar = amount / 100;
			cent = amount % 100;

			// display the year and the amount
		    System.out.printf("%4d%20d.%2d\n", year, dollar, cent);
		} // end for
	} // end main
} // end class Interest
