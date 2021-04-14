import java.util.Scanner;

/**
 * ex40
 * 
 * Suponha que o conceito de um aluno seja determinado em função da sua nota.
Suponha, também, que esta nota seja um valor inteiro na faixa de 0 a 100,
conforme a seguinte faixa:
Nota        Conceito
0 a 49      Insuficiente
50 a 64     Regular
65 a 84     Bom
85 a 100    Ótimo

Crie um algoritmo que apresente o conceito e a nota do aluno.
 */
public class ex40 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // lê a nota do aluno
        System.out.print("Qual é a nota do aluno? ");
        double nota = scanner.nextDouble();

        // apresenta o conceito do aluno
        System.out.print("Conceito do Aluno -> ");

        // verifica o conceito do aluno
        if ( nota >= 0 && nota <= 49) {
            System.out.println("\033[1;31mINSUFICIENTE.\033[m");
        } else if (nota >= 50 && nota <= 64) {
            System.out.println("\033[1;32mREGULAR\033[m");
        } else if (nota >= 65 && nota <= 84) {
            System.out.println("\033[1;33mBOM\033[m");
        } else {
            System.out.println("\033[1;34mÓTIMO\033[m");
        }

        // fecha a classe 'Scanner'
        scanner.close();
    }
}