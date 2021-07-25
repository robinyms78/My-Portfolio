import java.util.Scanner;

public class Product 
{
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		int x, y, z;
		int result;
		
		Scanner input = new Scanner(System.in);
		System.out.println("Please enter the first integer: ");
		x = input.nextInt();
		
		System.out.println("Please enter the second integer: ");
		y = input.nextInt();
		
		System.out.println("Please enter the third integer: ");
		z = input.nextInt();
		
		result = x * y * z;
		
		System.out.printf("Product is %d\n", result);
	}
}
