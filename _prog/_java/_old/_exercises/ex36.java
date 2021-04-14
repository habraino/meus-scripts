import java.util.Scanner;

/**
 * ex36
 * 
 * 
 * Escreva um algoritmo que, para uma conta bancária, leia o seu número, o saldo,
o tipo de operação a ser realizada (depósito ou retirada) e o valor da operação.
Após, determine e mostre o novo saldo. Se o novo saldo ficar negativo, deve ser
mostrada, também, a mensagem “conta estourada”.
 */
public class ex36 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);


        // declaração das variáveis
        int numero;
        int tipoOperacao;
        double saldo;
        double valorOperacao;
        double novoSaldo = 0;

        // lê o número do titular
        System.out.print("Informe o número do titular: ");
        numero = scanner.nextInt();

        // lê o saldo do titular
        System.out.print("Informe o saldo do titular: ");
        saldo = scanner.nextDouble();

        // pergunta o tipo da operação do titular
        System.out.print("Tipo de operação [1=depositar, 2=sacar]: ");
        tipoOperacao = scanner.nextInt();

        // pergunta o valor da operação
        System.out.print("Informe o valor da operação escolhida: ");
        valorOperacao = scanner.nextDouble();

        // fecha a classe 'Scanner'
        scanner.close();

        // verifica o tipo de operação do titular
        if (tipoOperacao == 1) {
            novoSaldo = saldo + valorOperacao;
        } else if (tipoOperacao == 2) {
            novoSaldo = saldo - valorOperacao;
        }

        // apresenta os dados na tela
        System.out.printf("Numero do titular: %d%n", numero);
        System.out.printf("Saldo inicial: R$ %.2f%n",saldo);

        // verifica se novoSaldo é positivo ou não
        if (novoSaldo < 0) {
            System.out.println("Conta estourada!");
        } else {
            System.out.printf("Novo saldo: R$ %.2f%n", novoSaldo);
        }

    }
}