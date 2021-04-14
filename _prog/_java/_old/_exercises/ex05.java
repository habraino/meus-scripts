/**
 * ex05
 * 
 * Faça um algoritmo que:
    a) Obtenha o valor para a variável HT (horas trabalhadas no mês);
    b) Obtenha o valor para a variável VH (valor hora trabalhada):
    c) Obtenha o valor para a variável PD (percentual de desconto);
    d) Calcule o salário bruto => SB = HT * VH;
    e) Calcule o total de desconto => TD = (PD/100)*SB;
    f) Calcule o salário líquido => SL = SB – TD;
    g) Apresente os valores de: Horas trabalhadas, Salário Bruto, Desconto, Salário
    Liquido.
 */

import java.util.Scanner;

public class ex05 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        double HT, VT, PD, SB, TD, SL;

        /* lê a hora trabalhada */
        System.out.print("Horas Trabalhadas: ");
        HT = scanner.nextDouble();

        /* lê o valor por cada hora trabalhada */
        System.out.print("Valor hora trabalhada: ");
        VT = scanner.nextDouble();

        /* lê o percentual de desconto */
        System.out.print("Percentual de desconto: ");
        PD = scanner.nextDouble();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula o salário bruto */
        SB = HT * VT;

        /* calculao o total de desconto */
        TD = (PD * 100) / SB;

        /* calcula o salário liquido */
        SL = SB - TD;
        
        //Horas trabalhadas, Salário Bruto, Desconto, Salário Liquido
        /* apresenta o resultado */
        System.out.println("*************************************************");
        System.out.printf("Horas trabalhadas................: %.2fNdb%n",HT);
        System.out.printf("Salário Bruto....................: %.2fNdb%n",SB);
        System.out.printf("Desconto de......................: %.2f%s\n",TD, "%");
        System.out.printf("Salário Liquido..................: %.2fNdb%n",SL);
        System.out.println("*************************************************");

    }
    
}

