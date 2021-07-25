package pkg;

// Fig. 3.14: AccountTest.java
// Inputting and outputting floating-point numbers with Account objects.

import java.util.Scanner;

public class AccountTest 
{
	// main method begins execution of Java application
	public static void main(String[] args) 
	{
		Account account1 = new Account(50.00); // create Account object
		Account account2 = new Account(-7.53); // create Account object

		// display initial balance of each object
		System.out.printf("account balance: %.2f\n",
			account1.getBalance());
		System.out.printf("account balance: %.2f\n\n",
			account2.getBalance());

		// create Scanner to obtain input from command window
		Scanner input1 = new Scanner(System.in);
		Scanner input2 = new Scanner(System.in);
		double depositAmount; // deposit amount read from user
		double withdrawalAmount; // withdrawal amount read from user

		System.out.print("Enter deposit amount for account1: "); // prompt
		depositAmount = input1.nextDouble(); // obtain user input
		System.out.printf("\nadding %.2f to account1 balance\n\n",
			depositAmount); 
		account1.credit(depositAmount); // add to account1 balance
		
		// display balance
		System.out.printf("account balance: $%.2f\n",
			account1.getBalance());
		System.out.printf("account balance: $%.2f\n\n",
			account2.getBalance());

	    System.out.print("Enter withdrawal amount for account1: "); // prompt
		withdrawalAmount = input1.nextDouble(); // obtain user input
		System.out.printf("\nsubtracting %.2f from account1 balance\n\n",
			withdrawalAmount); 
		account1.debit(withdrawalAmount); // subtract from account1 balance
		
		// display balance
		System.out.printf("account balance: $%.2f\n",
			account1.getBalance());
		System.out.printf("account balance: $%.2f\n\n",
			account2.getBalance());

	    System.out.print("Enter deposit amount for account2: "); // prompt
		depositAmount = input1.nextDouble(); // obtain user input
		System.out.printf("\nadding %.2f to account2 balance\n\n",
			depositAmount); 
		account2.credit(depositAmount); // add to account2 balance
		
		// display balance
		System.out.printf("account balance: $%.2f\n",
			account1.getBalance());
		System.out.printf("account balance: $%.2f\n\n",
			account2.getBalance());

	    System.out.print("Enter withdrawal amount for account2: "); // prompt
		withdrawalAmount = input1.nextDouble(); // obtain user input
		System.out.printf("\nsubtracting %.2f from account2 balance\n\n",
			withdrawalAmount); 
		account2.debit(withdrawalAmount); // subtract from account2 balance
		
		// display balance
		System.out.printf("account balance: $%.2f\n",
			account1.getBalance());
		System.out.printf("account balance: $%.2f\n\n",
			account2.getBalance());
	} // end main
} // end class AccountTest
