/**
 * ex16
 * 
 * Faça um algoritmo que leia a velocidade de um veículo em km/h e calcule e
    imprima a velocidade em m/s (metros por segundo).
 */

import java.util.Scanner;

public class ex16 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração da variável */
        int vel, novaVel;

        /* lê a velocidade em Km/h */
        System.out.print("Informe a velocidade em km/h: ");
        vel = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* converte a velocidade de km/h para m/s */
        novaVel = vel * 1060;

        /* apresenta o resultado */
        System.out.printf("Velocidade em (metros por segundo): %dm/s%n", novaVel);
        

    }
}