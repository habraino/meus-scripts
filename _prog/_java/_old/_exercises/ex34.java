import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * ex34
 * 
 * Uma empresa irá dar um aumento de salário aos seus funcionários de acordo
com a categoria de cada empregado. O aumento seguirá a seguinte regra:
• Funcionários das categorias A, C, F, e H ganharão 10% de aumento sobre o
salário;
• Funcionários das categorias B, D, E, I, J e T ganharão 15% de aumento sobre
o salário;
• Funcionários das categorias K e R ganharão 25% de aumento sobre o salário;
• Funcionários das categorias L, M, N, O, P, Q e S ganharão 35% de aumento
sobre o salário;
• Funcionários das categorias U, V, X, Y, W e Z ganharão 50% de aumento
sobre o salário.
Faça um algoritmo que escreva nome, categoria e salário reajustado de cada
empregado.
 */
public class ex34 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        List<String> categoria1 = Arrays.asList(ct1);
        List<String> categoria2 = Arrays.asList(ct2);
        List<String> categoria3 = Arrays.asList(ct3);
        List<String> categoria4 = Arrays.asList(ct4);

        String nome;
        double salario;
        double salarioReajustado = 0;
        int categoria;


        /* lê o nome da pessoa */
        System.out.print("Informe o nome da pessoa: ");
        nome = scanner.next();

        /* lê o salário da pessoa */
        System.out.print("Informe o salário da pessoa: ");
        salario = scanner.nextDouble();

        /* apresenta as categorias na tela */
        mostraCategoria(categoria1, 1);
        mostraCategoria(categoria2, 2);
        mostraCategoria(categoria3, 3);
        mostraCategoria(categoria4, 4);

        /* pede para usuário informar sua categoria */
        System.out.print("És de que categoria? [1-4] ");
        categoria = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /** 
         * verifica as categoria para efetuar o reajuste salarial
         */
        if (categoria == 1) {
            salarioReajustado = salario + (salario * 10) / 100;
        } else if (categoria == 2) {
            salarioReajustado = salario + (salario * 15) / 100;
        } else if (categoria == 3) {
            salarioReajustado = salario + (salario * 35) / 100;
        } else if (categoria == 4) {
            salarioReajustado = salario + (salario * 50) / 100;
        }

        /* apresenta os dados finais */
        System.out.printf("Nome.....................: %s%n",nome);
        System.out.printf("Salário..................: %.2f%n",salario);
        System.out.printf("Salário reajustado.......: %.2f%n",salarioReajustado);
        System.out.printf("Categoria................: %dª%n",categoria);
        

    }

    /* método para apresentar as categorias */
    public static void mostraCategoria(List<String> list, int pos) {
        System.out.printf("%dª categoria: ",pos);
        list.forEach(x -> System.out.printf("%s ", x));
        System.out.println();
    }

    /**
     * lista das categorias
     */
    public static String[] ct1 = {
        "A", "C", "F", "H"
    };

    public static String[] ct2 = {
        "B", "D", "E", "I", "J",  "T"
    };
    
    public static String[] ct3 = {
        "L", "M", "N", "O", "P", "Q", "S"
    };

    public static String[] ct4 = {
        "U", "V", "X", "Y", "W",  "Z"
    };
}

