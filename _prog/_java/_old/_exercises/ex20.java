/**
 * ex20
 * 
 * Admitindo que uma data é lida pelo algoritmo em uma variável inteira, e não em
uma variável do tipo data, crie um algoritmo que leia uma data no formato
DDMMAA e imprima essa data no formato AAMMDD, onde:
• A letra D corresponde a dois algarismos representando o dia;
• A letra M corresponde a dois algarismos representando o mês;
• A letra A corresponde aos dois últimos algarismos representando o ano.
 */

import java.util.Scanner;

public class ex20 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int d, m, a;

        /* lê o dia */
        System.out.print("Dia: ");
        d = scanner.nextInt();

        /* lê o mês */
        System.out.print("Mês: ");
        m = scanner.nextInt();

        /* lê o ano */
        System.out.print("Ano: ");
        a = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* mostra no formato aammdd */
        System.out.printf("%d-0%d-%d%n", a, m, d);

    }
}


