/**
 * ex01
 * 
 * Faça um algoritmo para calcular a área de uma circunferência, considerando a
    fórmula ÁREA = π * RAIO 2 . Utilize as variáveis AREA e RAIO, a constante π (pi = 3,14159) e os operadores aritméticos de multiplicação.
 */

import java.util.Scanner;


public class ex01 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scaner' */
        Scanner scan = new Scanner(System.in);
        
        /* declaração das variáveis */
        final double PI = 3.14159;
        double RAIO = 0;
        double AREA = 0;

        /* lê o raio */
        System.out.print("Informe o raio: ");
        RAIO = scan.nextDouble();

        /* fecha a classe Scanner */
        scan.close();

        /* calcula a área */
        AREA = PI * (RAIO * RAIO);

        /* mostra o resutado na tela */
        System.out.printf("A área da circunferência é de: %.2f%n",AREA);

    }
}


