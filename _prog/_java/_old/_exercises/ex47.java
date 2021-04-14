import java.util.Scanner;

/**
 * ex47
 * 
 * Elaborar um algoritmo que lê dois valores a e b e os escreve com a mensagem:
“São múltiplos” ou “Não são múltiplos”.
 */
public class ex47 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        int a, b;

        /* lê o primeiro valor */
        System.out.print("Informe o primeiro valor: ");
        a = scanner.nextInt();

        /* lê o segundo valor */
        System.out.print("Informe o segundo valor: ");
        b = scanner.nextInt();

        // verifica se são multiplos ou não
        if ( a % b == 0 || b % a == 0) {
            System.out.println("\033[1;33mSão múltiplos.\033[m");
        } else {
            System.out.println("\033[1;31mNão são múltiplos.\033[m");
        }

        // fecha a classe 'Scanner'
        scanner.close();
    }
}