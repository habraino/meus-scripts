import java.util.Scanner;

/**
 * ex25
 * 
 * Construa um algoritmo que receba como entrada três valores e os imprima em
ordem crescente.
 */
public class ex25 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* delcaração das variáveis */
        int n1, n2, n3;
        
        /* lê o primeiro valor */
        System.out.print("Informe o 1ª valor: ");
        n1 = scanner.nextInt();

        /* lê o segundo valor */
        System.out.print("Informe o 2ª valor: ");
        n2 = scanner.nextInt();

        /* lê o terceiro valor */
        System.out.print("Informe o 3ª valor: ");
        n3 = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* faz a verificações para imprimir na ordem crescente */
        if (n1 > n2 && n2 > n3) {
            System.out.printf("Em ordem crescente: %d -> %d -> %d%n", n3, n2, n1);
        } else if (n1 < n2 && n2 < n3) {
            System.out.printf("Em ordem crescente: %d -> %d -> %d%n", n1, n2, n3);
        } else if (n1 < n3 && n3 < n2) {
            System.out.printf("Em ordem crescente: %d -> %d -> %d%n", n1, n3, n2);
        } else if (n1 > n2 && n1 < n3) {
            System.out.printf("Em ordem crescente: %d -> %d -> %d%n", n2, n1, n3);
        } else if (n1 > n2 && n1 > n3 && n3 > n2) {
            System.out.printf("Em ordem crescente: %d -> %d -> %d%n", n2, n3, n1);
        }
    }
}