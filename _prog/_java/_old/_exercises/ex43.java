import java.util.Scanner;

/**
 * ex43
 * 
 * Faça um algoritmo que leia três números e mostre-os em ordem decrescente.
 */
public class ex43 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        int n1, n2, n3;

        // lê o primeiro valor
        System.out.print("Informe o primeiro valor: ");
        n1 = scanner.nextInt();

        // lê o segundo valor
        System.out.print("Informe o segundo valor: ");
        n2 = scanner.nextInt();

        // lê o terceiro valor
        System.out.print("Informe o terceiro valor: ");
        n3 = scanner.nextInt();

        // faz as verificações para apresentar na ordem decrescente
        if ((n1 > n2 && n2 > n3)) {
            System.out.printf("Ordem decrescente: %d -> %d -> %d%n", n1, n2, n3);
        } else if(n2 > n1 && n1 > n3) {
            System.out.printf("Ordem decrescente: %d -> %d -> %d%n", n2, n1, n3);
        } else if (n3 > n1 && n3 > n2 && n2 > n1) {
            System.out.printf("Ordem decrescente: %d -> %d -> %d%n", n3, n2, n1);
        } else if ((n3 > n1 && n3 > n2 && n1 > n2)) {
            System.out.printf("Ordem decrescente: %d -> %d -> %d%n", n3, n1, n2);
        } else if (n1 < n2 && n2 > n3 && n3 > n1) {
            System.out.printf("Ordem decrescente: %d -> %d -> %d%n", n2, n3, n1);
        } else if (n1 > n2 && n2 < n3) {
            System.out.printf("Ordem decrescente: %d -> %d -> %d%n", n1, n3, n2);
        }

        // fecha a classe 'Scanner'
        scanner.close();
    }
}