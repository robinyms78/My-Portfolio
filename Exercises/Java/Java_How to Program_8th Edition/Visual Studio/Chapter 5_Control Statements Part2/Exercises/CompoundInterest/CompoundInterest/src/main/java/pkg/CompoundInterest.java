// Ex. 5.13: CompoundInterest.java

package pkg;

public class CompoundInterest 
{
	public static void main(String[] args) 
	{
		double amount; // amount on deposit at end of each year
		double principal = 1000.0; // initial amount before interest 

		// display headers

		System.out.printf("%4s%10s%20s\n", "Year", "Rate", "Amount on deposit");
		// calculate amount on deposit for each of ten years
	    for (int year = 1; year <= 10; year++)
		{
			// calculate amount on deposit for each interest rate
			for (int rate = 5; rate <= 10; rate++)
			{
				// calculate new amount for specified year
				amount = principal * Math.pow(1.0 + (float)rate/100, year);

				// display the year and the amount
				System.out.printf("%4d%10.2f%,20.2f\n", year, (float)rate/100, amount);
			} // end outer for
		} // end inner for	
	} // end main
} // end class CompoundInterest
