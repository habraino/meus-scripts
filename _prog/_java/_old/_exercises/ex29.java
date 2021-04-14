import java.util.Scanner;

/**
 * ex29
 * 
 * Faça um algoritmo que leia os valores A, B e C. Mostre uma mensagem que
informe se a soma de A com B é menor, maior ou igual a C.
 */
public class ex29 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int a, b, c;
        int soma;

        /* lê o primerio valor */
        System.out.print("Informe o primerio valor: ");
        a = scanner.nextInt();

        /* lê o segundo valor */
        System.out.print("Informe o segundo valor: ");
        b = scanner.nextInt();

        /* lê o terceiro valor */
        System.out.print("Informe o terceiro valor: ");
        c = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        soma = a + b;

        /* faz as verificações */
        if (soma > c) {
            System.out.println("A soma de A e B é maior que C.");
        } else if(soma < c) {
            System.out.println("A soma de A e B é menor que C.");
        } else {
            System.out.println("A soma de A e B é igual a C.");
        }
    }
}

