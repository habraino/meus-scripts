import java.util.Scanner;

/**
 * ex23
 * 
 * Faça um algoritmo que leia um número N e imprima “F1”, “F2” ou “F3”, conforme
a condição:
    • “F1”, se N <= 10
    • “F2”, se N > 10 e N <= 100
    • “F3”, se n > 100
 */
public class ex23 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração da variável */
        int n;

        /* lê um número inteiro qualquer */
        System.out.print("Informe um número inteiro: ");
        n = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* verifica as condições */
        if (n <= 10) {
            System.out.println("F1");
        } else if(n > 10 && n <= 100) {
            System.out.println("F2");
        } else {
            System.out.println("F3");
        }


    }
}