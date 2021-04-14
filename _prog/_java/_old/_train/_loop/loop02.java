import java.util.Scanner;

/**
 * loop02
 */
public class loop02 {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);

        int valor = 0;

        System.out.print("Informe um valor inteiro: ");
        valor = scan.nextInt();
        //int cont = 1;

        // enquanto o valor esitver fora do intervalo [10, 100]
        while((valor < 10) || (valor > 100) ){
            System.out.print("Informe um valor inteiro: ");
            valor = scan.nextInt();
        }
        System.out.println("Valor correto!!");

    }
}