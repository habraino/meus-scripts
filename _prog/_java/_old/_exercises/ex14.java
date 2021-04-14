/**
 * ex14
 * 
 * Faça um algoritmo que leia dois valores inteiros (A e B) e apresente o           resultado
    da soma do quadrado de cada valor lido.
 * 
 */

import java.util.Scanner;

public class ex14 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int a, b;
        int somaQuadrado;

        /* lê o primeiro valor */
        System.out.print("Informe o primeiro valor: ");
        a = scanner.nextInt();

        /* lê o segundo valor */
        System.out.print("Informe o segundo valor: ");
        b = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula a soma do quadrado dos valores lidos */
        somaQuadrado = (a * a) + (b * b);

        System.out.printf("O resultado de %d² + %d² = %d%n",a, b, somaQuadrado);

    }
    
}