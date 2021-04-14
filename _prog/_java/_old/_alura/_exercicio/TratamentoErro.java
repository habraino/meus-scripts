import java.util.*;



/**
 * TratamentoErro
 */

public class TratamentoErro {

    // método que retorna divisão entre dois números
    public static double div(double n, double d) throws ArithmeticException
    {
        
        return n / d;
    }

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        boolean cont = true;

        while (cont) {
            try {
                System.out.print("Informe o númerador: ");
                double num = scanner.nextInt();

                System.out.print("Informe o númerador: ");
                double de = scanner.nextInt();

                double result = div(num, de);

                System.out.printf("Result: %.2f\n", result);
                cont = false;

            } catch (InputMismatchException e) {
                System.err.printf("\nException: %s\n",e);
                scanner.nextLine();

                System.out.println("You must enter integers.Please try again.\n");
            } catch (ArithmeticException ar) {
                System.err.printf("\nException: %s\n",ar);
                System.out.println("Zero is an invalid denominator. Plase try again.\n");
            }
        }

    }
}