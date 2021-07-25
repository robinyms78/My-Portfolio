import java.util.Scanner;

public class EmployeeTest 
{

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		Employee employee1 = new Employee("Johnson", "Smith", 3000);
		Employee employee2 = new Employee("Robin", "Yap", 2000);
		
		System.out.printf("Employee 1's yearly salary: $%.2f\n", employee1.getSalary());
		System.out.printf("Employee 2's yearly salary: $%.2f\n", employee2.getSalary());
		
		employee1.increment();
		employee2.increment();
		
		System.out.printf("Employee 1's new yearly salary: $%.2f\n", employee1.getSalary());
		System.out.printf("Employee 2's new yearly salary: $%.2f\n", employee2.getSalary());
	}
}
