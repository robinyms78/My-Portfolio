package pkg;

// Fig. 3.13: Account.java
// Account class with a constructor to validate and
// initialize instance variable balance of type double

public class Account 
{
	private double balance; // instance variable that stores the balance

	// constructor
	public Account(double initialBalance)
	{
		// validate that initialBalance is greater than 0.0;
		// if it is not, balance is initialized to the default value 0.0
		if (initialBalance > 0.0)
			balance = initialBalance;
	} // end Account constructor

	// credit (add) an amount to the account
	public void credit(double amount)
	{
		balance = balance + amount; // add amount to balance
	} // end credit method

	// debit (subtract) an amount from the account
	public void debit(double amount)
	{
		if (amount < getBalance())
			balance = balance - amount; // subtract amount from balance
		if (amount > getBalance())
			balance = balance; // balance remain unchanged
			System.out.println("Debit amount exceeded account balance");
	} // end debit method

	// return the account balance
	public double getBalance()
	{
		return balance; // gives the value of balance to the calling method
	} // end method getBalance
} // end class account
