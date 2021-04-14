/**
 * ex22
 * 
 * Faça um algoritmo que leia dois números A e B e imprima o maior deles.
 */

import java.util.Scanner; 

public class ex22 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int n1, n2;

        /* lê o primeiro número */
        System.out.print("Entre com primeiro número: ");
        n1 = scanner.nextInt();

        /* lê o segundo número */
        System.out.print("Entre com segundo número: ");
        n2 = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* verifica qual é o maior */
        if (n1 > n2) {
            System.out.printf("%d é maior%n", n1);
            System.out.printf("%d é menor%n", n2);
        } else if(n2 > n1) {
            System.out.printf("%d é maior%n", n2);
            System.out.printf("%d é menor%n", n1);
        }
        
    }
}