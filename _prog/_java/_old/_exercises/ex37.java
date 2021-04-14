import java.util.Scanner;

/**
 * ex37
 * 
 * Um hotel cobra R$ 60.00 a diária e mais uma taxa de serviços. A taxa de
serviços é de:
• R$ 5.50 por diária, se o número de diárias for maior que 15;
• R$ 6.00 por diária, se o número de diárias for igual a 15;
• R$ 8.00 por diária, se o número de diárias for menor que 15.
Construa um algoritmo que mostre o nome e o total da conta de um cliente.
 */
public class ex37 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        final double precoFixo = 60;
        double taxa = 0;
        double precoTotal = 0;
        int dia;
        String nome;

        // lê o nome do cliente
        System.out.print("Nome do cliente: ");
        nome = scanner.next();

        // lê o dia a ficar hospedado
        System.out.print("Vais ficar hospedado por quantos dias? ");
        dia = scanner.nextInt();

        // verifica quantidade de dias para calcular a taxa
        if ( dia > 15) {
            taxa = 5.50;
        } else if ( dia < 15) {
            taxa = 8.00;
        } else {
            taxa = 6.00;
        }

        // calcula o preço total a pagar
        precoTotal = (precoFixo * dia) + taxa;

        System.out.printf("Nome do cliente: %s%n", nome);
        System.out.printf("Total da conta do cliente: R$ %.2f%n", precoTotal);


        // fecha a classe 'Scanner'
        scanner.close();

    }
}