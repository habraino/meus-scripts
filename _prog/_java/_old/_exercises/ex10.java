/**
 * ex10
 * 
 * Faça um algoritmo que leia dois valores para as variáveis A e B e efetue a       troca
    dos valores de forma que a variável A passe a possuir o valor da variável B e a
    variável B passe a possuir o valor da variável A. Apresente os valores trocados.
 */

import java.util.Scanner;

public class ex10 {

    public static void main(String[] args) {

        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);
        
        /* declaração das variáveis */
        int a;
        int b;

        /* lê o primeiro valor */
        System.out.print("Informe o primeiro valor: ");
        a = scanner.nextInt();

        /* lê o segundo valor */
        System.out.print("Informe o segundo valor: ");
        b = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* efetua as possíveis trocas */
        efetuaTroca(a, b);


    }

    /* método para efetuar troca */
    public static void efetuaTroca(int x, int y) {
        int a;
        int b;
        a = y;
        b = x;

        System.out.printf("Primeiro valor: %d%n",a);
        System.out.printf("Segundo valor: %d%n",b);
    }
}