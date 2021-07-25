// Reads the user's weight and height, then calculates and displays the user's body mass index

import java.util.Scanner;

public class BMI {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		
		double weight;
		double height;
		double BMI;
		
		System.out.print("Enter your weight in kg: ");
		weight = input.nextDouble();
		
		System.out.print("Enter your height in m: ");
		height = input.nextDouble();
		
		BMI = weight / (height * height);
		System.out.printf("Your body mass index is %f\n", BMI);
		System.out.print("BMI VALUES\n");
		System.out.print("Underweight: less than 18.5\n");
		System.out.print("Normal     : between 18.5 and 24.9\n");
		System.out.print("Overweight : between 25 and 29.9\n");
		System.out.print("Obese:     : 30 or greater\n");
	}
}
