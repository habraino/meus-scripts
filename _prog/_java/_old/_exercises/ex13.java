/**
 * ex13
 * 
 * Faça um algoritmo que leia dois valores inteiros (A e B) e apresente o          resultado
    do quadrado da soma dos valores lidos.
 */

import java.util.Scanner;

public class ex13 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int a, b;
        int quadradoSoma;

        /* lê o primeiro valor */
        System.out.print("Informe o primeiro valor: ");
        a = scanner.nextInt();

        /* lê o segundo valor */
        System.out.print("Informe o segundo valor: ");
        b = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula o quadrado da soma dos valores lidos */
        quadradoSoma = (a * a) + (2 * a * b) + (b * b);

        System.out.printf("O resultado de (%d + %d)² = %d%n", a, b, quadradoSoma);


    }
    
}