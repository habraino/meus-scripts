import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

/**
 * Aula03
 */
public class Aula03 {

    public static void main(String[] args) {
        List<String> lista = Arrays.asList(
            "Banana",
            "Fruta-Pão",
            "Manga",
            "Ananás",
            "Caju",
            "Jaca"
        );
        /*
        for(String i : lista){
            System.out.println(i);
        }
        */
        List<String> lista2 = new ArrayList<String>();
        lista2.add("Computer");
        lista2.add("Keyboard");

        /*
        lista2.forEach(p -> {
            System.out.println(lista2.get(1));
        });
        */

        //lista2.forEach(x -> System.out.println(x));
        lista.forEach(System.out::println);
    }
}