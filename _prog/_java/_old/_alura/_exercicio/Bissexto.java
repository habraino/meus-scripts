import java.util.Scanner;

/**
 * Bissexto
 */
public class Bissexto {

    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);

        int num = 0;

        System.out.print("Informe um valor: ");
        num = in.nextInt();

        if((num % 4 == 0 && num % 100 != 0) || (num % 400 == 0))
            System.out.printf("O ano %d é bissexto\n", num);
        else
            System.out.printf("O ano %d não é bissexto\n", num);

    }
}