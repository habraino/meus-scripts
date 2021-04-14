import java.util.Scanner;

/**
 * ex48
 * 
 * Escreva um algoritmo que leia o código de um aluno e suas três notas. Calcule a
média ponderada do aluno, considerando que o peso para a maior nota seja 4 e
para as duas restantes, 3. Mostre o código do aluno, suas três notas, a média
calculada e uma mensagem: "APROVADO" se a média for maior ou igual a 5 e
"REPROVADO" se a média for menor que 5.
 */
public class ex48 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        double n1, n2, n3;
        double media;
        int codigo;

        // lê o código do aluno
        System.out.print("Informe o código do aluno: ");
        codigo = scanner.nextInt();

        // lê a primeira nota
        System.out.print("Informe a 1ª nota: ");
        n1 = scanner.nextDouble();

        // lê a segunda nota
        System.out.print("Informe a 2ª nota: ");
        n2 = scanner.nextDouble();

        // lê a terceira nota
        System.out.print("Informe a 3ª nota: ");
        n3 = scanner.nextDouble();
        
        // calcula a media do aluno
        media = ((n1 * 0.04) + (n2 * 0.03) + (n3 * 0.3));

        // apresenta os dados na tela
        System.out.println("O código do aluno é..: "+codigo);
        System.out.println("1ª nota..............: "+n1);
        System.out.println("2ª nota..............: "+n2);
        System.out.println("3ª nota..............: "+n3);
        System.out.printf("Media................: %.2f%n",media);

        // verfica a posição do aluno
        if (media >= 5) {
            System.out.println("APROVADO");
        } else {
            System.out.println("REPROVADO");
        }

        // fecha a classe 'Scanner'
        scanner.close();
    }
}