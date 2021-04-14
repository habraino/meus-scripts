import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * ex33
 * 
 * Uma pessoa comprou quatro artigos em uma loja. Para cada artigo, tem-se
nome, preço e percentual de desconto. Faça um algoritmo que imprima nome,
preço e preço com desconto de cada artigo e o total a pagar.
 */
public class ex33 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        String nome = "";
        double pd;
        double preco = 0;
        double novoPreco;
        double total = 0;
        int cont = 1;

        List<String> nomes = new ArrayList<>();
        List<Number> precos = new ArrayList<>();
        List<Number> precosDesconto = new ArrayList<>();

        /* faz varedura de 4 artigos */
        while (cont <= 4) {
            System.out.println("*****************************************");
            System.out.printf("\t\t%dº Artigo\n", cont);
            System.out.println("*****************************************");
            /* lê o nome da pessoa */
            System.out.print("Nome do artigo: ");
            nome = scanner.next();
            nomes.add(nome);

            /* lê o preço do produto */
            System.out.print("Preço do artigo: ");
            preco = scanner.nextDouble();
            precos.add(preco);

            /* lê o percentual do desconto */
            System.out.print("Percentual de desconto: ");
            pd = scanner.nextDouble();

            /* fecha a classe Scanner */
            scanner.close();

            /* calcula o novo preço com desconto */
            novoPreco = preco - (preco * pd) / 100;
            precosDesconto.add(novoPreco);

            /* calcula o preço total */
            total += novoPreco;

            cont++;
        }

        /* apresenta os resultados */
        System.out.println("*************************************************");
        for(int i = 0; i < 4; i++) {
            System.out.println("*************************************************");
            System.out.printf("\t\t%dº Artigo\n", i+1);
            System.out.println("*************************************************");
            System.out.println("Nome do Artigo...................: "+nomes.get(i));
            System.out.println("Preço do Artigo..................: R$ "+precos.get(i));
            System.out.println("Preço com desconto...............: R$ "+precosDesconto.get(i));
            System.out.println("*************************************************");
        }
        System.out.println("Total a pagar................: R$ "+total);
        System.out.println("*************************************************");
        
    }
}