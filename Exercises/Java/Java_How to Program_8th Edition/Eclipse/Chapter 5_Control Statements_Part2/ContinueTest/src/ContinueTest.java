public class ContinueTest 
{

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		for (int count = 1; count <= 10; count++)
		{
			if (count == 5)
				continue;
			
			System.out.printf("%d ", count);
		}
		
		System.out.println("\nUsed continue to skip printing 5");
	}
}
