/**
 * ex02
 * 
 * Faça um algoritmo que calcule a área de um triângulo, considerando a fórmula

    Área = (BASE * ALTURA) / 2
    Utilize as variáveis AREA, BASE e ALTURA e os
operadores aritméticos de multiplicação e divisão.
 * 
 */

import java.util.Scanner;

public class ex02 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scan = new Scanner(System.in);

        /* declaração das variáveis */
        double AREA, BASE, ALTURA; 

        /* lê a base */
        System.out.print("Informe a base: ");
        BASE = scan.nextDouble();

        /* lê a altura */
        System.out.print("Informe a altura: ");
        ALTURA = scan.nextDouble();

        /* fecha a classe Scanner */
        scan.close();

        /* calcula a altura do triângulo */
        AREA = (BASE * ALTURA) / 2;

        /* mostra o resultado na tela */
        System.out.printf("A área do triângulo é: %.2f%n", AREA);

    }
}