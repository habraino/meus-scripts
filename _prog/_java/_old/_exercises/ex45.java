import java.util.Scanner;

/**
 * ex45
 * 
 * Calcule a média aritmética das três notas de um aluno e mostre, além do valor
da média, uma mensagem de "Aprovado", caso a média seja igual ou superior a
10; a mensagem “em prova final” caso a média seja menor que 9 e maior ou igual
a 7; e "reprovado", caso contrário.
 */
public class ex45 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das notas
        int cont = 1;
        int soma = 0;
        double notas = 0;
        double media = 0;

        // executa 3 vezes consecutivos
        while (cont <= 3) {
            // lê as 3 notas
            System.out.printf("Informe a %dª nota: ",cont);
            notas = scanner.nextDouble();

            soma += notas;// faz o acumulo das notas

            cont++;// incrementa o contador
        }

        // calcula a média
        media = soma / cont;

        // mostra a média na tela
        System.out.printf("Média: %.2f%n",media);

        // verifica o estado do aluno
        if (media >= 10) {
            System.out.println("APROVADO");
        } else if (media >= 7 && media <= 9) {
            System.out.println("EM PROVA FINAL");
        } else {
            System.out.println("REPROVADO");
        }

        // fecha a classe 'Scanner'
        scanner.close();
    }
}