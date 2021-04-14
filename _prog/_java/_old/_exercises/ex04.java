/**
 * ex04
 * 
 * Faça um algoritmo que:
    a) Leia um número inteiro;
    b) Leia um segundo número inteiro;
    c) Efetue a adição dos dois valores;
    d) Apresente o valor calculado.
 */


import java.util.Scanner;

public class ex04 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int num1, num2, soma;

        /* lê o primeiro número */
        System.out.print("Informe o primeiro valor: ");
        num1 = scanner.nextInt();

        /* lê o segundo número */
        System.out.print("Informe o segundo valor: ");
        num2 = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* efetua a soma entre o valores obtidos */
        soma = num1 + num2;

        /* apresenta o resultado */
        System.out.println("A soma é: "+soma);


    }
}