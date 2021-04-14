import java.util.Scanner;

public class aula02 {

    public static void main(final String[] args) {
        
        int num1;
        int num2;
        int sum;

        Scanner in = new Scanner(System.in);

        System.out.print("Enter first number: ");
        num1 = in.nextInt();

        System.out.print("Enter second number: ");
        num2 = in.nextInt();

        sum = num1 + num2;

        System.out.println("Sum is: "+sum);

    }
}