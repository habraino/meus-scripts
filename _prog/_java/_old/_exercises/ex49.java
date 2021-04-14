import java.util.Scanner;

/**
 * ex49
 * 
 * Faça um algoritmo que leia um número inteiro e mostre uma mensagem
indicando se este número é par ou ímpar e se é positivo ou negativo.
 */
public class ex49 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração da variável
        int num;

        // lê um número qualquer
        System.out.print("Informe um número qualquer: ");
        num = scanner.nextInt();

        // faz a análise do número lido
        if (num > 0) {
            System.out.println("O número é POSITIVO.");
        } else if (num < 0) {
            System.out.println("O número é NEGATIVO.");
        } 
        if (num == 0) {
            System.out.println("O número é NEUTRO.");
        } else {
            // verifica a paridade do número
            if (num % 2 == 0) {
                System.out.println("E é PAR.");
            } else {
                System.out.println("E é ÍMPAR.");
            }
        }
        // fecha a classe 'Scanner'
        scanner.close();
    }
}