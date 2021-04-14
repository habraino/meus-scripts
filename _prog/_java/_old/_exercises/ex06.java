/**
 * ex06
 * 
 * Faça um algoritmo que leia uma temperatura em graus Celsius e apresente-a
    convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160)5,
    na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius;
 */

import java.util.Scanner;

public class ex06 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);
        
        /* declaração das variáveis */
        double C = 0;
        double F = 0;

        /* lê temperatura em gráus Celsius */
        System.out.print("Em︒C: ");
        C = scanner.nextDouble();

        /* fecha a classe Scanner */
        scanner.close();

        /* converte em graus Fahrenheit */
        F = (9 * C + 160) / 5;

        /* mostra o resultado */
        System.out.printf("Convertida em︒F vem: %.2f%n", F);



    }
}