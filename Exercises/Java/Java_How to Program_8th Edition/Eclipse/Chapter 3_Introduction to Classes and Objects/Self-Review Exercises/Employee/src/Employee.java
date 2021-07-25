public class Employee 
{
	private String firstName;
	private String lastName;
	private double salary;
	
	public Employee (String first, String last, double initialSalary)
	{
		firstName = first;
		lastName = last;

		if (initialSalary > 0.0)
			salary = initialSalary;
	}
	
	public void setFirstName (String name)
	{
		firstName = name;
	}
	
	public void setLastName(String name)
	{
		lastName = name;
	}
	
	public void setSalary(double pay)
	{
		salary = pay;
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
		return salary;
	}
	
	public void increment()
	{
		salary = salary * 1.1;
	}
	
}
