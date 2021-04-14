/**
 * ex12
 * 
 * Faça um algoritmo que leia um valor inteiro e apresente os resultados do
    quadrado e do cubo do valor lido.
 */

import java.util.Scanner;


public class ex12 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declarção da variável */
        int num;

        /* lê um valor inteiro qualquer */
        System.out.print("Informe um valor inteiro qualquer: ");
        num = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* apresenta o quadrado do valor lido */
        System.out.printf("O quadrado do número %d é %d.%n", num, (num*num));

        /* apresenta o cubo do valor lido */
        System.out.printf("O cubo do número %d é %d.%n", num, (num*num*num));
    }
}