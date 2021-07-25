public class Scope 
{
	private int x = 1;
	
	public void begin()
	{
		int x = 5;
		
		System.out.printf("local x in method begin is %d\n", x);
		
		useLocalVariable();
		useField();
		useLocalVariable();
		useField();
		
		System.out.printf("\nlocal x in method begin is %d\n", x);
	}
	
	public void useLocalVariable()
	{
		int x = 25;
		
		System.out.printf("\nlocal x on entering method useLocalVariable is %d\n", x);
		++x;
		System.out.printf("local x before exiting method useLocalVariable is %d\n", x);
	}
	
	public void useField()
	{
		System.out.printf("\nfield x on entering method useField is %d\n", x);
		x *= 10;
		System.out.printf("field x before exiting method useField is %d\n", x);
	}
}
