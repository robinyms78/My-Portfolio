import java.util.Scanner;

public class Credit 
{
	public void creditCalculator() 
	{
		int accountNumber;
		int beginningBalance;
		int newBalance;
		int charges;
		int totalCharges = 0;
		int credits;
		int totalCredits = 0;
		int creditLimit = 0;
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("Please enter your account number:");
		accountNumber = input.nextInt();
		
		System.out.println("Please enter your beginning account balance:");
		beginningBalance = input.nextInt();
		
		System.out.println("Please enter your charges for each item or -1 to quit:");
		charges = input.nextInt();
		
		System.out.println("Please enter your credit or -1 to quit:");
		credits = input.nextInt();
		
		while (charges != -1)
		{
			System.out.println("Please enter your charges for each item or -1 to quit:");
			charges = input.nextInt();
			
			totalCharges += charges;
		}
		
		while (credits != -1)
		{
			System.out.println("Please enter your credit for each item or -1 to quit:");
			credits = input.nextInt();
			
			totalCredits += credits;
		}
			
		newBalance = beginningBalance + totalCharges - totalCredits;
		
		System.out.printf("Your new balance for account %d is %d\n", accountNumber, newBalance);
		
		if (newBalance > creditLimit)
			System.out.println("Credit limit exceeded!");
	}
}
