import java.util.Scanner;

/**
 * ex26
 * 
 * Considere que o último concurso vestibular apresentou três provas: Português,
Matemática e Conhecimentos Gerais. Considerando que para cada candidato
tem-se um registro contendo o seu nome e as notas obtidas em cada uma das
provas, construa um algoritmo que forneça:
a) o nome e as notas em cada prova do candidato
b) a média do candidato
c) uma informação dizendo se o candidato foi aprovado ou não. Considere que
um candidato é aprovado se sua média for maior que 7.0 e se não apresentou
nenhuma nota abaixo de 5.0
 */
public class ex26 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        String nome;
        String resultado;
        double port, math, conheGerais;
        double media;


        /* lê o nome do candidato */
        System.out.print("Nome do candidato: ");
        nome = scanner.nextLine();

        /* lê a nota da L.Portuguesa */
        System.out.print("Português: ");
        port = scanner.nextDouble();

        /* lê a nota da matemática */
        System.out.print("Matemática: ");
        math = scanner.nextDouble();

        /* lê a nota de conhecimento gerais */
        System.out.print("Conhecimento Gerais: ");
        conheGerais = scanner.nextDouble();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula a média do aluno */
        media = (port + math + conheGerais) / 3;

        /* verifica o resultado do aluno */
        if (port >= 10 && math >= 10 && conheGerais >= 10 && media >= 10) {
            resultado = "Aprovado";
        } else {
            resultado = "Reprovado";
        }

        /* apresenta os resultados */
        System.out.printf("Nome.............: %s%n", nome);
        System.out.printf("Média............: %.2f%n", media);
        System.out.printf("Resultado........: %s%n", resultado);
        
    }
}