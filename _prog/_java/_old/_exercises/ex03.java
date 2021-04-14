/**
 * ex03
 * 
 * Faça um algoritmo que:
    a) Leia o nome;
    b) Leia o sobrenome;
    c) Concatene o nome com o sobrenome;
    d) Apresente o nome completo.
 */

import java.util.Scanner;

public class ex03 {

    public static void main(String[] args) {
       
        /* cria uma nova instância do 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        String nome, sobreNome, nomeCompleto;

        /* lê o nome */
        System.out.print("Informe o seu nome: ");
        nome = scanner.nextLine();

        /* lê o sobreNome */
        System.out.print("Informe o seu sobrenome: ");
        sobreNome = scanner.nextLine();

        /* fecha a classe Scanner */
        scanner.close();

        /* concatena o nome com apelido */
        nomeCompleto = String.format("%s %s", nome, sobreNome);

        /* mostra o nome completo */
        System.out.println("Nome completo: "+nomeCompleto);

    }
}