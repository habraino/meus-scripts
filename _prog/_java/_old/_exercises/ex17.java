/**
 * ex17
 * 
 * Faça um algoritmo que leia dois números inteiros (Int1 e Int2) e imprima o
    quociente e o resto da divisão inteira de Int1 por Int2.
 */

import java.util.Scanner;

public class ex17 {

    public static void main(String[] args) {

        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int n1, n2;
        double div;

        /* lê o primeiro valor */
        System.out.print("Informe o primeiro valor: ");
        n1 = scanner.nextInt();

        /* lê o segundo valor */
        System.out.print("Informe o segundo valor: ");
        n2 = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* efetua o quociente entre os valores */
        div = n1 / n2;

        /* apresenta o quociente entre os valores */
        System.out.printf("O quociente os valores é: %.2f%n", div);

        /* apresenta o resto da divisão inteira */
        System.out.printf("O resto da divisão inteira: %d%n", (n1 % n2));


    }
}