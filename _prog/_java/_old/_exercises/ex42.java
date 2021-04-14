import java.util.Scanner;

/**
 * ex42
 * 
 * Faça um algoritmo que leia dois números e indique se são iguais ou se são
diferentes. Mostre o maior e o menor (nesta sequência).
 */
public class ex42 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        int num1, num2;
        int maior = 0;
        int menor = 0;

        // lê o primeiro número 
        System.out.print("Informe o primeiro valor: ");
        num1 = scanner.nextInt();

        // lê o segundo número 
        System.out.print("Informe o segundo valor: ");
        num2 = scanner.nextInt();

        // verifica se os nums são iguais
        if (num1 == num2) {
            System.out.println("Os números lidos são iguais.");
        } else {
            System.out.println("Os números são diferentes.");
            //verifica o maior/menor número 
            if (num1 > num2) {
                maior = num1;
                menor = num2;
            } else {
                maior = num2;
                menor = num1;
            }
            System.out.println("Maior: "+maior);
            System.out.println("Menor: "+menor);
        }

        // fecha a classe 'Scanner'
        scanner.close();

    }
}