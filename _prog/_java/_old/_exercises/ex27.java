import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * ex27
 * 
 * Uma empresa de vendas tem três corretores. A empresa paga ao corretor uma
comissão calculada de acordo com o valor de suas vendas. Se o valor da venda
de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor
vendido. Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$
50.000.00 (incluindo extremos) a comissão será de 9.5%. Em qualquer outro
caso, a comissão será de 7%. Escreva um algoritmo que gere um relatório
contendo nome, valor da venda e comissão de cada um dos corretores. O
relatório deve mostrar também o total de vendas da empresa.
 */
public class ex27 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        List<String> nomes = new ArrayList<>();
        List<Number> vendas = new ArrayList<>();
        List<Number> comiList = new ArrayList<>();
        String nome;
        double valorVenda;
        double comissao;
        boolean sair = false;
        double total = 0;

        /* enquanto verdadeiro */
        while (!sair) {
            /* lê o nome da pessoa */
            System.out.print("Nome: ");
            nome = scanner.next();
            nomes.add(nome);

            /* lê o preço da venda */
            System.out.print("Preço da Venda: ");
            valorVenda = scanner.nextDouble();
            vendas.add(valorVenda);

            /* calcula a comissão da pessoa */
            if (valorVenda == 50000) {
                comissao = (valorVenda * 12) / 100;
                comiList.add(comissao);
            } else if (valorVenda > 30000 && valorVenda < 50000) {
                comissao = (valorVenda * 9.5) / 100;
                comiList.add(comissao);
            } else {
                comissao = (valorVenda * 7) / 100;
                comiList.add(comissao);
            }

            /* calcula o preço total da venda */
            total += valorVenda;

            /* pergunta ao usuário se pretende continuar */
            String cont;
            System.out.print("continuar? [s/n]: ");
            cont = scanner.next().toLowerCase();

            /* verifica a escola do usuário  */
            if ("n".equals(cont)) {
                sair = true; /* interrompe a execução */
            }
        }

        /* fecha a classe Scanner */
        scanner.close();

        /* apresenta o relatório na tela */
        System.out.println("**********************************************");
        for(int i = 0; i < nomes.size(); i++) {
            System.out.println("Nome.....................: "+nomes.get(i));
            System.out.printf("Comissão.................: R$ %.0f%n",comiList.get(i));
            System.out.println("**********************************************");
        }
        System.out.println("**********************************************");
        System.out.printf("Total Venda..............: R$ %.0f%n",total);
        System.out.println("**********************************************");
    }
}