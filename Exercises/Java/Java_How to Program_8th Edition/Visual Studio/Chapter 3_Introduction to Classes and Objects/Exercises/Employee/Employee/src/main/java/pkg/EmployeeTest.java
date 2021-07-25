package pkg;

public class EmployeeTest 
{
	public static void main(String[] args) 
	{
		Employee employee1 = new Employee("Yap", "Robin", 0.0);
		Employee employee2 = new Employee("Nakamura", "Kumiko", 0.0);

		employee1.setSalary(6000.0);
		employee2.setSalary(3000.0);
		employee1.displaySalary();
		employee2.displaySalary();
		employee1.displayNewSalary();
		employee2.displayNewSalary();
	}
}
