
/**
 * ex07
 * 
 * Faça um algoritmo que leia uma temperatura em Fahrenheit e a apresente
    convertida em graus Celsius. A fórmula de conversão é C = (F – 32) * ( 5 / 9), na
    qual F é a temperatura em Fahrenheit e C é a temperatura em Celcius.
 */
import java.util.Scanner;


public class ex07 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);
        
        /* declaração das variáveis */
        double c = 0;
        double f = 0;

        /* lê temperatura em gráus Fahrenheit */
        System.out.print("Em︒F: ");
        f = scanner.nextDouble();

        /* fecha a classe Scanner */
        scanner.close();

        /* converte em graus Celsius */
        c = (f - 32) * (5 / 9);

        /* mostra o resultado */
        System.out.printf("Convertida em︒C vem: %.2f\n", c);

    }

}


