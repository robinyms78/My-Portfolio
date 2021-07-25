package pkg;

import javax.swing.JOptionPane;

public class Addition 
{
	public static void main(String[] args) 
	{
		// prompt user to enter first integer
		int number1 =
			Integer.parseInt(JOptionPane.showInputDialog("Enter first integer"));

		// prompt user to enter seconf integer
		int number2 =
			Integer.parseInt(JOptionPane.showInputDialog("Enter second integer"));

		// calculate sum
		int sum = number1 + number2;

		// create the message
		String message =
			String.format("Sum is %s", sum);

		// display sum
		JOptionPane.showMessageDialog(null, message);
	}
}
