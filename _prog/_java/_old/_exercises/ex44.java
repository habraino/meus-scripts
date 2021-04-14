import java.util.Scanner;

/**
 * ex44
 * 
 * Faça um algoritmo que leia quatro números (Opção , Num1 , Num2 e Num3) e
mostre o valor de Num1 se Opção for igual a 2; o valor de Num2 se Opção for
igual a 3; e o valor de Num3 se Opção for igual a 4. Os únicos valores possíveis
para a variável Opção são 2, 3 e 4.
 */ 
public class ex44 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        int cont = 0;
        int opt = 0;
        int[] num = new int[3];

        // lê a opção
        System.out.print("Informe a sua opção[2,3,4]: ");
        opt = scanner.nextInt();

        // executa quatros vezes
        while (cont < 3) {
            // lê os números
            System.out.printf("Informe o %dº valor: ", cont+1);
            num[cont] = scanner.nextInt();

            cont++; // incrementa o contador
        }

        // verifica as opções

        if (opt == 2) {
            System.out.println("Número: "+num[0]);
        } else if(opt == 3) {
            System.out.println("Número: "+num[1]);
        } else {
            System.out.println("Número: "+num[2]);
        }


        // fecha a classe 'Scanner'
        scanner.close();
    }
}