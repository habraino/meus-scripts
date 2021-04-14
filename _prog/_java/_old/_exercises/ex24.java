import java.util.Scanner;

/**
 * ex24
 * 
 * O sistema de avaliação de determinada disciplina, é composto por três provas. A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Faça
um algoritmo para calcular a média final de um aluno desta disciplina.
 */
public class ex24 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int n1, n2, n3;
        double media;

        /* lê a primeira nota */
        System.out.print("Informe a 1ª nota: ");
        n1 = scanner.nextInt();

        /* lê a segunda nota */
        System.out.print("Informe a 2ª nota: ");
        n2 = scanner.nextInt();

        /* lê a terceira nota */
        System.out.print("Informe a 3ª nota: ");
        n3 = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula a média final do aluno */
        media = (n1 + n2 + n3) / 3;

        System.out.printf("A média final é: %.2f%n", media);
    }
}