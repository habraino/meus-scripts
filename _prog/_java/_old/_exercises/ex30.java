import java.util.Scanner;

/**
 * ex30
 * 
 * Suponha que um caixa disponha apenas de notas de 1, 10 e 100 reais.
Considerando que alguém está pagando uma compra, escreva um algoritmo que
mostre o número mínimo de notas que o caixa deve fornecer como troco. Mostre
também: o valor da compra, o valor do troco e a quantidade de cada tipo de nota
do troco. Suponha que o sistema monetário não utilize moedas.
 */
public class ex30 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int nt1 = 1, nt10 = 10, nt100 = 100;
        double troco;
        int cont100 = 0;
        int cont10 = 0;
        int cont1 = 0;
        double pagamento;
        double preco;

        /* lê o valor do pagamento */
        System.out.print("Qual é o preço do produto? ");
        preco = scanner.nextDouble();
        /* lê o valor do pagamento */
        System.out.print("Efetue o pagamento? ");
        pagamento = scanner.nextDouble();

        /* fecha a classe Scanner */
        scanner.close();

        /* faz o pagamento para verificar o troco */
        troco = preco - pagamento;

        System.out.println("*************************************************");

        /* mostra o valor da compra */
        System.out.printf("O valor da compra é de: R$ %.2f%n", preco);

        /* mostra o troco */
        System.out.printf("O troco é de: R$ %.0f%n", troco);

        /* faz as possíveis verificações para efetuar o troco */
        if (troco <= 0) { /* se não tiver troco */
            System.out.println("Quantidade de cada tipo de nota do troco:");
            System.out.printf("%d nota(s) de R$ %d\n", cont100, nt100);
            System.out.printf("%d nota(s) de R$ %d\n", cont10, nt10);
            System.out.printf("%d nota(s) de R$ %d\n", cont1, nt1);
        } else { /* caso tiver */
            /* efetua os calculos para distribuir quantidade das notas do troco */
            while (troco > 0.0) { 
                if (troco >= nt100) {
                    troco -= nt100;
                    cont100++;
                } else if (troco >= nt10 && troco < nt100) {
                    troco -= nt10;
                    cont10++;
                } else if (troco < nt10){
                    troco -= nt1;
                    cont1++;
                } else {
                    cont1 = 0;
                    cont10 = 0;
                    cont100 = 0;
                }
            }
            /* apresenta o resultado com os possíveis troco */
            System.out.println("Quantidade de cada tipo de nota do troco:");
            System.out.printf("%d nota(s) de R$ %d\n", cont100, nt100);
            System.out.printf("%d nota(s) de R$ %d\n", cont10, nt10);
            System.out.printf("%d nota(s) de R$ %d\n", cont1, nt1);
        }
        System.out.println("*************************************************");
    }
}