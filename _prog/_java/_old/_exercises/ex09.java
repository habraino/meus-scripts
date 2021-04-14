/**
 * ex09
 */

/*
Faça um algoritmo que calcule a quantidade de litros de combustível gasta em
uma viagem, utilizando um automóvel que faz 12Km por litro. Para obter o
cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média
durante ela. Desta forma, será possível obter a distância percorrida com a
fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância,
basta calcular a quantidade de litros de combustível utilizada na viagem com a
fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os
valores da velocidade média, tempo gasto na viagem, a distância percorrida e a
quantidade de litros utilizada na viagem.
*/

import java.util.Scanner;

public class ex09 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int TEMPO;
        double VELOCIDADE;
        double DISTANCIA;
        double LITROS_USADOS;

        /* lê o tempo gasto */
        System.out.print("Informe o tempo gasto: ");
        TEMPO = scanner.nextInt();

        /* lê a velocidade */
        System.out.print("Informe a velocidade média: ");
        VELOCIDADE = scanner.nextDouble();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula a distância percorrida */
        DISTANCIA = TEMPO * VELOCIDADE;

        /* calcula quantidade de litros usado durante a viagem */
        LITROS_USADOS = DISTANCIA / 2;

        /* apresentando os resultados */
        System.out.println("*********************************************");
        System.out.printf("Tempo gasto...................: %d horas%n", TEMPO);
        System.out.printf("Velocidade média..............: %.0fKm/hora%n", VELOCIDADE);
        System.out.printf("Distância percorrida..........: %.0fKm%n", DISTANCIA);
        System.out.printf("Listros usados................: %.2f litros%n", LITROS_USADOS);
        System.out.println("*********************************************");

    }
}

