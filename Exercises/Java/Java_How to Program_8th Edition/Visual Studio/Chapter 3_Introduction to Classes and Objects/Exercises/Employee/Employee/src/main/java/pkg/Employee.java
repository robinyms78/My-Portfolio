package pkg;

public class Employee 
{
	private String firstName;
	private String lastName;
	private double salary;

	public Employee(String nameFirst, String nameLast, double amount)
	{
		firstName = nameFirst;
		lastName = nameLast;
		salary = amount;
	}

	public void setSalary(double amount)
	{
		if (amount > 0) // set monthly salary if salary is negative
			salary = amount;
	}

	public String getFirstName()
	{
		return firstName;
	}

	public String getLastName()
	{
		return lastName;
	}

	public double getSalary()
	{
		double yearlySalary = salary * 12;
		return yearlySalary;
	}

	public void displaySalary()
	{
		System.out.printf("%s %s's yearly salary is %.2f\n", getFirstName(), getLastName(), getSalary());
	}

	public double getNewSalary()
	{
		double newYearlySalary = salary * 1.1 * 12;
		return newYearlySalary;
	}

	public void displayNewSalary()
	{
		System.out.printf("%s %s's new yearly salary is %.2f\n", getFirstName(), getLastName(), getNewSalary());
	}

}
