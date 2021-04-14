import java.lang.management.MemoryManagerMXBean;
import java.util.Scanner;

/**
 * ex38
 * 
 * Faça um algoritmo que leia 3 números inteiros distintos e escreva o menor deles.
 */
public class ex38 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        int num;
        int menor = 0;
        int cont = 1;

        while (cont <= 3) {
            // lê os 3 números distintos
            System.out.printf("Informe o %dº valor: ",cont);
            num = scanner.nextInt();

            // verifica o menor número
            if (cont == 1) {
                menor = num;
            } else if (num < menor) {
                menor = num;
            }

            cont++; // incrementa o contador
        }

        // apresenta o menor valor lido 
        System.out.printf("O menor valor lido é: %d%n",menor);

        // fecha a classe 'Scanner'
        scanner.close();
    }
}