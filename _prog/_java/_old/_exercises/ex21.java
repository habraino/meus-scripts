/**
 * ex21
 * 
 * Suponha que uma escola utilize, como código de matrícula, um número inteiro
no formato AASDDD, onde:
• Os dois primeiros dígitos, representados pela letra A, são os dois últimos
algarismos do ano da matrícula;
• O terceiro dígito, representado pela letra S, vale 1 ou 2, conforme o aluno
tenha se matriculado no 1º ou 2º semestre;
• Os quatro últimos dígitos, representados pela letra D, correspondem à ordem
da matrícula do aluno, no semestre e no ano em questão.
Crie um algoritmo que leia o número de matrícula de um aluno e imprima o ano
e o semestre em que ele foi matriculado.
 */

import java.util.Scanner;

public class ex21 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int aa, s, dddd;
 
        /* lê o ano da martícula */
        System.out.print("Os dois últimos algarismos do ano da martícula: ");
        aa = scanner.nextInt();

        /* lê o semeste da martícula */
        System.out.print("O semeste da martícula(1 = 1º, 2 = 2º): ");
        s = scanner.nextInt();

        /* lê a ordem da martícula */
        System.out.print("A ordem da martícula (4 digítos): ");
        dddd = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* apresenta o resultado */
        System.out.printf("%d%d%d%n", aa, s, dddd);

    }
}