import java.util.List;
import java.util.Scanner;
import java.util.Arrays;
import java.util.function.Predicate;

/**
 * Aula04
 */
public class Aula04 {

    public static void filtro(List<String> list, Predicate<String> condicao){
        /*for(String i : list){
            if(condicao.test(i)){
                System.out.println(i);
            }
        }*/
        list.stream().filter((str) -> condicao.test(str))
          //  .forEach((i) -> System.out.println(i));
            .forEach(System.out::println);
    }
    public static void main(String[] args) {
        String busca;
        Scanner scan = new Scanner(System.in);

        List<String> lista = Arrays.asList(
            "Neves", "Guadalupe", "Pantufo", 
            "Roça Lembá", "Ponta Figo",
            "Generosa", "Almeirim", "Ponta Furada",
            "Ribeira Funda", "Conde", "Ilhêu",
            "Santo Amaro", "Moro Peixe", "Porto Alegre"
        );

        System.out.print("Procurar cidade por letra inicial: ");
        busca = scan.nextLine();

        System.out.println("Cidades que começam com '"+busca.toUpperCase()+"'");
        filtro(lista, (s) -> s.startsWith(busca.toUpperCase())); 

        System.out.println("\nCidades que terminam com 'a'");
        filtro(lista, (s) -> s.endsWith("a"));

        System.out.println("\nImprime a lista completa");
        filtro(lista, (s) -> true);

        System.out.println("\nNão imprime a lista");
        filtro(lista, (s) -> false);

        System.out.println("\nImprime somente os que têm + que 10 carateres");
        filtro(lista, (s) -> s.length() > 10);
    }
}
