import java.util.Scanner;

/**
 * loop06
 * 
 * venda de tablets
 */
public class loop06 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double price = 0; // armazena o preço de cada unidade
        int quant = 0; // armazena quantidade de unidades vendidas
        double totPrice = 0; // armazena o preço total
        double stock = 0;

        // lê e armazena o valor de cada unidade
        System.out.print("Informe o valor de uma unidade de tablet: ");
        price = scan.nextDouble();

        // equanto o preço informado for inválido
        while(price < 0){
            System.out.print("Erro. Digite um valor válido: ");
            price = scan.nextDouble();
        }

        System.out.print("Quantos tablets tu vai levar? ");
        quant = scan.nextInt();

        // calcula o preço total
        totPrice = price * quant;

        // calcula o lucro da empresa
        stock =  totPrice - (300 * quant);

        System.out.println("o preço total é: "+totPrice+"Dbs");

        // verifica o lucro da empresa
        if(stock > 0){
            System.out.println("Lucro de "+stock+"Dbs");
        }else if(stock == 0){
            System.out.println("Não houve lucro!");
        }else{
            System.out.println("Déficit de: "+stock+"Dbs");
        }

    }
}