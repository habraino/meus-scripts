/**
 * ex18
 * 
 * 
 * Considere a seguinte situação: descontam-se inicialmente 10% do salário bruto
do trabalhador como contribuição à previdência social. Após esse desconto, há
um outro desconto de 5% sobre o valor restante do salário bruto, a título de um
determinado imposto. Faça um algoritmo que leia o salário bruto de um cidadão e
imprima o seu salário líquido.
 */

import java.util.Scanner;

public class ex18 {

    public static void main(String[] args) {
        
         /* cria uma nova instância da classe 'Scanner' */
         Scanner scanner = new Scanner(System.in);

         /* declaração das variáveis */
         double SB, SL;

        /* lê o salário bruto de um cidadão */
        System.out.print("Informe o salário bruto: ");
        SB = scanner.nextDouble();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula o salário líquido docidadão */
        SL = SB - (SB * 15) / 100;

        /* apresenta o resultado na tela */
        System.out.printf("Salário Líquido do cidadão: %.2f%n", SL);

    }
}