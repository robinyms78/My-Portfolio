import java.util.Scanner;

public class RoundingNumbers 
{
	public void roundingOff()
	{
		double x;
		int y;
		
		Scanner input = new Scanner(System.in);
	
		System.out.println("Please enter the value:");
		x = input.nextDouble();
		y = (int) Math.floor(x + 0.5);
		
		System.out.printf("The original number is %.2f and rounded off number is %d\n", x, y);
				
	}
}
