import java.util.Scanner;

/**
 * ex31
 * 
 * Uma empresa produz três tipos de peças mecânicas: parafusos, porcas e
arruelas. Têm-se os preços unitários de cada tipo de peça e sabe-se que sobre
estes preços incidem descontos de 10% para porcas, 20% para parafusos e 30%
para arruelas. Escreva um algoritmo que calcule o valor total da compra de um
cliente. Deve ser mostrado o nome do cliente. O número de cada tipo de peça
que o mesmo comprou, o total de desconto e o total a pagar pela compra.
 */
public class ex31 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int contParafuso = 0;
        int contPorca = 0;
        int contArruela = 0;
        int quant;

        String nomeCliente = "";
        String tipoPreca = "";
        String opt = "";
        
        double precoPecas = 500;
        double precoTotal = 0;
        double totDesconto = 0;
        boolean sair = false;


        /* lê o nome do individo */
        System.out.print("Informe o seu nome: ");
        nomeCliente = scanner.nextLine();

        /* começa a compra */
        while (!sair) {
            /* apresenta as peças disponíveis */
            System.out.println("****************************************");
            System.out.println("Produtos disponíveis:");
            System.out.println("    Parafuso (desconto de 10%)");
            System.out.println("    Porca    (desconto de 20%)");
            System.out.println("    Arruela  (desconto de 30%)");
            System.out.println("****************************************");
            System.out.println("O preço fixo para cada peça é R$ 500.");
            System.out.println("****************************************");

            /* pede para cliente informar sua escolha */
            System.out.print("O que desejas comprar? ");
            tipoPreca = scanner.next();

            /* quantidade de produto a ser comprado */
            System.out.printf("Quantos(as) %s vais levar? ", tipoPreca);
            quant = scanner.nextInt();

            /* verifica tipo da peça comprada */
            if (tipoPreca.toLowerCase().equals("parafuso")) {
                totDesconto += (precoPecas * 0.10);
                contParafuso += quant;
                precoTotal += contParafuso * precoPecas;
            } else if (tipoPreca.toLowerCase().equals("porca")) {
                totDesconto += (precoPecas * 0.20);
                contPorca += quant;
                precoTotal += contPorca * precoPecas;
            } else if (tipoPreca.toLowerCase().equals("arruela")) {
                totDesconto += (precoPecas * 0.30);
                contArruela += quant;
                precoTotal += contArruela * precoPecas;
            } else {
                System.out.println("Produto indisponível!!");
            }

            /* pergunta pro cliente se deseja continuar com a compra */
            System.out.print("continuar [s/n]: ");
            opt = scanner.next();

            /* fecha a classe Scanner */
            scanner.close();

            /* verifica se o cliente deseja continuar */
            if (opt.toLowerCase().equals("n")) {
                sair = true;
            }

        }

        System.out.println("**************************************************");
        System.out.println("\t\tDados do cliente");
        System.out.println("**************************************************");
        System.out.println("Nome...................: "+nomeCliente);
        System.out.println("Peças compradas...");
        System.out.println("Parafuso................: "+contParafuso);
        System.out.println("Porca...................: "+contPorca);
        System.out.println("Arruela.................: "+contArruela);
        System.out.printf("Preço fixo das peças....: R$ %.2f\n", precoPecas);
        System.out.printf("Preço Total.............: R$ %.2f\n", precoTotal);
        System.out.printf("Total desconto..........: R$ %.2f\n", totDesconto);
        System.out.println("**************************************************");
        
    }
}

