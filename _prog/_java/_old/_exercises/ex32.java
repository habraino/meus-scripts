import java.util.Scanner;

/**
 * ex32
 * 
 * A revendedora de carros Pica-Pau Ltda. paga aos seus funcionários vendedores
dois salários mínimos fixos, mais uma comissão fixa de R$ 50,00 por carro
vendido e mais 5% do valor das vendas. Faça um algoritmo que determine o
salário total de um vendedor.
 */
public class ex32 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* delcaração das variáveis */
        double salario;
        double precoCarro;
        double aumento;

        /* lê o salário do funcionário */
        System.out.print("Informe o salário do funcionário: ");
        salario = scanner.nextDouble();

        /* lê o preço do carro vendido */
        System.out.print("Qual é o preço do carro? ");
        precoCarro = scanner.nextDouble();

        /* fecha a classe Scanner */
        scanner.close();
    
        /* calcula o aumento do funcionário */
        aumento = ((precoCarro * 0.05) + 50.0);

        /* calcula o SB do funcionário */
        salario += aumento;
        System.out.printf("O salário bruto do funcionário é: %.2f\n", salario);
        
    }
}