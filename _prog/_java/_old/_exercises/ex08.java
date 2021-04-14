/**
 * ex08
 * 
 * Faça um algoritmo que calcule e apresente o valor do volume de uma lata de
    óleo, utilizando a fórmula VOLUME = 3,14159 * RAIO 2 * ALTURA.
 * 
 */

import java.util.Scanner;


public class ex08 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        double ALTURA;
        final double PI = 3.14159;
        double RAIO;
        double VOLUME;

        /* lê raio da lata */
        System.out.print("O raio da lata: ");
        RAIO = scanner.nextDouble();

        /* lê a altura da lata */
        System.out.print("A altura da lata: ");
        ALTURA = scanner.nextDouble();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula o volume da lata */
        VOLUME = PI * (RAIO * RAIO) * ALTURA;

        /* apresenta o resultado */
        System.out.printf("O volume da leta é: %.2f%n", VOLUME);

    }
}


