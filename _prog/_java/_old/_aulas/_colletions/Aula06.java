import java.util.Arrays;
import java.util.List;
import java.util.ListIterator;
import java.util.Collections;
import java.util.LinkedList;
/**
 * Aula06
 */
public class Aula06 {

    public static void main(String[] args) {
        
        String[] name = {"John", "Matheus", "Brayen", "Habraino"}; 
        List<String> list = new LinkedList<>(Arrays.asList(name));

        
        ListIterator<String> iterator = list.listIterator();
        
        while (iterator.hasNext()) {
            String next = iterator.next();
            iterator.set(next.concat(" Gomes").toUpperCase());
        }
        System.out.println(list);
        

        // cria uma nova lista vazia
        String[] lin = new String[10];
        LinkedList<String> links = new LinkedList<>(Arrays.asList(lin));

        // preenche a lista completa só com 'Python'
        Collections.fill(links, "Python");
        System.out.println(links);

        // troca todo 'Python' por 'Java'
        Collections.replaceAll(links, "Python", "Java");
        System.out.println(links);

        // efetua cópia da list e adiciona no links
        Collections.copy(links, list);
        System.out.println(links);

        // retorna a frequência do 'Python'
        int freq = Collections.frequency(links, "Java");
        System.out.printf("Frequência do Java: %d%n",freq);

        // verifica se as listas têm algo em comum
        boolean comum = Collections.disjoint(list, links);
        System.out.println("As listas têm algo em comum? "+comum);

    }
}