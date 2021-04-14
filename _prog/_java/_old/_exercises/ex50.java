import java.util.Scanner;

/**
 * ex50
 * 
 * O cardápio de uma lanchonete é o seguinte:
Preço unitário              Especificação
100 Cachorro quente             1,10
101 Bauru simples               1,30
102 Bauru c/ovo                 1,50
103 Hamburger                   1,10
104 Cheeseburger                1,30
105 Refrigerante                1,00

Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule
o valor a ser pago por aquele lanche. Considere que a cada execução somente
será calculado um item.
 */
public class ex50 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        int item;
        int quant;
        double preco = 0;

        
        
        // apresenta o cardápio
        System.out.println("|===============================================|");
        System.out.printf("|Preço unitário         |     Especificação     |\n");
        System.out.println("|===============================================|");
        System.out.println("|1 -> Cachorro quente   |          1,10         |");
        System.out.println("|2 -> Bauru simples     |          1,30         |");
        System.out.println("|3 -> Bauru c/ovo       |          1,50         |");
        System.out.println("|4 -> Hamburger         |          1,10         |");
        System.out.println("|5 -> Cheeseburger      |          1,30         |");
        System.out.println("|6 -> Refrigerante      |          1,00         |");
        System.out.println("================================================|");
        
        // lê o item a ser pedido
        System.out.print("O que desejas comprar? [1 - 6]: ");
        item = scanner.nextInt();

        // lê a quantidade a ser comprada
        System.out.print("Quanto desejas comprar? ");
        quant = scanner.nextInt();

        // verifica o tipo de item comprado para calcular os preços
        switch (item) {
            case 1:
                preco = quant * 1.10;
                break;
            case 2:
                preco = quant * 1.30;
                break;
            case 3:
                preco = quant * 1.50;
                break;
            case 4:
                preco = quant * 1.10;
                break;
            case 5: 
                preco = quant * 1.30;
                break;
            case 6:
                preco = quant * 1.00;
                break;
            default:
                System.out.println("Item inválido!");
                break;
        }

        // mostra o preço total na tela
        System.out.printf("O preço total do lanche é: %.2f%n", preco);
        

        // fecha a classe 'Scanner'
        scanner.close();
    }
}