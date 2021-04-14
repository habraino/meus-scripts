import java.util.LinkedList;
import java.util.Arrays;

/**
 * Aula02
 */
public class Aula02 {

    public static void main(String[] args) {
        
        String[] colors = {"black", "green", "yellow"};
        LinkedList<String> links = new LinkedList<>(Arrays.asList(colors));

        links.addLast("pink");// adiciona no final da lista
        links.add(2, "blue");// adiciona na posição 2
        links.addFirst("white");

        for(String color : links){
            System.out.println(color);
        }


    }
}