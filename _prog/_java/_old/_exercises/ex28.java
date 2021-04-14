import java.util.Scanner;

/**
 * ex28
 * 
 * Escreva um algoritmo que determine o número de dias que uma pessoa já viveu.
Considere que um mês tenha 30 dias.
 */
public class ex28 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int dias, idade, nasc;
        int atual = 2020;    

        /* lê a data do nascimento da pessoa */ 
        System.out.print("Informe sua data de nascimento: ");
        nasc = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula idade da pessoa */
        idade = atual - nasc;

        /* calcula dias vivida pela pessoa */
        dias = idade * 365;

        /* mostra o resultado na tela */
        System.out.printf("A pessoa tem %d anos.%n", idade);
        System.out.printf("E já viveu %d dias.%n", dias);
    }
}