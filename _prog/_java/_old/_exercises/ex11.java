/**
 * ex11
 * 
 * Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e
    ALTURA e apresente o valor do volume de uma caixa retangular. Utilize para o
    cálculo a fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.
 */

import java.util.Scanner;

public class ex11 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int COMPRIMENTO, LARGURA, ALTURA;
        int VOLUME;

        /* lê o comprimento da caixa */
        System.out.print("Informe o comprimento da caixa: ");
        COMPRIMENTO = scanner.nextInt();

        /* lê a largura da caixa */
        System.out.print("Informe a largura da caixa: ");
        LARGURA = scanner.nextInt();

        /* lê a altura da caixa */
        System.out.print("Informe a altura da caixa: ");
        ALTURA = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula o volume da caixa */
        VOLUME = COMPRIMENTO * LARGURA * ALTURA;

        /* apresenta o volume da caixa */
        System.out.printf("%nO volume da caixa é: %ddm³%n", VOLUME);

    }
}