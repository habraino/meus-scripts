import java.util.Scanner;

/**
 * ex35
 * 
 Uma sorveteria vende tr�s tipos de picol�s. Sabendo-se que o picol� do tipo 1 �
vendido por R$ 0.50, o do tipo 2 por R$ 0.60 e o do tipo 3 por R$ 0.75, fa�a um
algoritmo que, para cada tipo de picol�, mostre a quantidade vendida e o total
arrecadado.
 */
public class ex35 {

    public static void main(String[] args) {
        
        /* cria uma nova inst�ncia da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declara��o das vari�veis */
        int tipo;
        double total = 0;
        int contTipo1 = 0;
        int contTipo2 = 0;
        int contTipo3 = 0;
        int quant = 0;
        String opt = "";
        boolean sair = false;

        /* enquanto verdadeiro fa�a */
        while (!sair) {
            // apresenta o tipo dos picol�s
            System.out.println("Tipos de Picole disponiveis:");
            System.out.println("Tipo 1: R$ 0,50\nTipo 2: R$ 0,60\nTipo 3: R$ 0,70");

            // pergunta para usu�rio o tipo de picol� desejado
            System.out.print("Qual tipo desejas comprar? ");
            tipo = scanner.nextInt();

            System.out.print("Quanto desejas comprar? ");
            quant = scanner.nextInt();

            // analisa o tipo para fazer as contagens 
            if (tipo == 1) {
                contTipo1 += quant;
                total += 0.50 * quant;
            } else if(tipo == 2) {
                contTipo2 += quant;
                total += 0.60 * quant;
            } else if (tipo == 3) {
                contTipo3 += quant;
                total += 0.70 * quant;
            } else {
                System.out.println("Escolha inv�lida!!");
            }

            // pergunta se usu�rio deseja continuar com a compra
            System.out.print("continuar? [s/n]: ");
            opt = scanner.next();

            // verifica a escolha do usu�rio
            if (opt.equalsIgnoreCase("n")) {
                sair = true;
            }   
        }

        // apresenta os dados na tela
        System.out.println("Quantidade de cada tipo vendido:");
        System.out.printf("Picole do tipo 1: %d%n",contTipo1);
        System.out.printf("Picole do tipo 2: %d%n",contTipo2);
        System.out.printf("Picole do tipo 3: %d%n",contTipo3);
        System.out.printf("Preco total: R$ %.2f%n",total);

        /* fecha a classe Scanner */
        scanner.close();


    }
}