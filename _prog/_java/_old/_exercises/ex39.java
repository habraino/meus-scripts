import java.util.Scanner;

/**
 * ex39
 * 
 * Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos
lados de um triângulo, e se forem, verificar se é um triângulo equilátero, isóscele
ou escaleno. Se eles não formarem um triângulo, escrever uma mensagem.
Antes da elaboração do algoritmo, torna-se necessário a revisão de algumas
propriedades e definições.
Propriedade – o comprimento de cada lado de um triângulo é menor do que a
soma dos comprimentos dos outros dois lados.
Definição 1 - chama-se de triângulo equilátero o que tem os comprimentos dos
três lados iguais;
Definição 2 - chama-se de triângulo isóscele o triângulo que tem os
comprimentos de dois lados iguais;
Definição 3 - chama-se triângulo escaleno o triângulo que tem os
comprimentos dos três lados diferentes.
 */
public class ex39 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        int x, y, z;

        // lê o primeiro valor
        System.out.print("Informe o primeiro lado do triângulo: ");
        x = scanner.nextInt();

        // lê o primeiro valor
        System.out.print("Informe o segundo lado do triângulo: ");
        y = scanner.nextInt();

        // lê o primeiro valor
        System.out.print("Informe o terceiro lado do triângulo: ");
        z = scanner.nextInt();
        
        // verifica se os lados podem formar um triângulo
        if ((x < y + z) && (y < x + z) && (z < x + y)) {
            System.out.print("Pode formar um triângulo -> ");

            // verifica o tipo de triângulo formado
            if (x == y && y == z) {
                System.out.println("EQUILÁTERO");
            } else if ((x == y && y != z) || (x == z && z != y) || (x != y && x != z && y == z)) {
                System.out.println("ISÓSCELES");
            } else {
                System.out.println("ESCALENO");
            }
        } else {
            System.out.println("Não pode formar um triângulo.");
        }
        

        // fecha a classe 'Scanner'
        scanner.close();
    }
}