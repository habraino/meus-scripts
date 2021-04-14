import java.util.Scanner;

/**
 * ex41
 * 
 * Faça um algoritmo que leia dois números e mostre qual o maior dos dois .
 */
public class ex41 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        int num1, num2;

        // lê o primeiro valor
        System.out.print("Informe o primeiro valor: ");
        num1 = scanner.nextInt();


        // lê o segundo valor
        System.out.print("Informe o segundo valor: ");
        num2 = scanner.nextInt();
        
        // verifica o maior entre os dois nums
        if (num1 > num2) {
            System.out.println("Maior é: "+num1);
        } else {
            System.out.println("Maior é: "+num2);
        }

        // fecha a classe 'Scanner'
        scanner.close();
    }
}