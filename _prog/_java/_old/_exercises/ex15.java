/**
 * ex15
 * 
 * Faça um algoritmo que leia dois números nas variáveis Val1 e Val2, calcule       sua
    média na variável Media e imprima seu valor.
 */

import java.util.Scanner;

public class ex15 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        double num1, num2;

        /* lê o primeiro valor */
        System.out.print("Informe a 1ª nota: ");
        num1 = scanner.nextDouble();

        /* lê o segundo valor */
        System.out.print("Informe a 2ª nota: ");
        num2 = scanner.nextDouble();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula a média aritimétrica entre os valores */
        double media = (num1 + num2) / 2;

        /* mostra o resultado */
        System.out.printf("A média é: %.2f%n", media);

    }
    
}