import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * TestaPessoa
 */
public class TestaPessoa {

    private static List<Pessoa> lista;
    private static Pessoa pessoa;

    private static String n;
    private static int i;
    private static Scanner scan;

    // método para ler todos os dados
    private static void obterTodos(List<Pessoa> list) {
        System.out.println("****************************************");
        for(Pessoa p : list){
            System.out.printf("\t\t%dª Pessoa\n", p.getId());
            System.out.println("****************************************");
            System.out.printf("Nome: %s\nIdade: %d\n", p.getNome(), p.getIdade());
            System.out.println("****************************************");
        }
    }
    public static void main(String[] args) {
        scan = new Scanner(System.in);
        lista = new ArrayList<>();
        int cont = 1;
        while (cont <= 4) {
            pessoa = new Pessoa();

            System.out.print("Nome: ");
            n = scan.next();
            pessoa.setNome(n);

            System.out.print("Idade: ");
            i = scan.nextInt();
            pessoa.setIdade(i);

            pessoa.setId(cont);

            // adiciona a pessoa na lista
            lista.add(pessoa);

            cont++;
        }    
        obterTodos(lista); // lê dados de todas as pessoas

    }
}


