// This program displays the course name and instructor name for GradeBook

#include <string>
using namespace std;

class GradeBook
{
public:
	GradeBook( string, string ); // Constructor for GradeBook
	void setInstructorName( string ); // Set instructor name for GradeBook
	void setCourseName( string ); // Set course name for GradeBook
	string getInstructorName(); // Get instructor name for GradeBook
	string getCourseName(); // Set course name for GradeBook
	void displayMessage(); // Display instructor and course name
private:
	string courseName;
	string instructorName;
};