public class GradeBookTest 
{

	public static void main(String[] args) 
	{
		GradeBook gradeBook1 = new GradeBook("CS101 Introduction to Java Programming", "Robin Yap");
		GradeBook gradeBook2 = new GradeBook("CS102 Data Structures in Java", "Johnson Smith");

		gradeBook1.displayMessage();
		gradeBook2.displayMessage();
	}
}
