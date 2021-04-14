import java.util.SortedSet;
import java.util.Arrays;
import java.util.TreeSet;

/**
 * Aula10
 */
public class Aula10 {

    public static void main(String[] args) {
        
        String[] colors = {
            "Green", "Red", "Blue", "Yellow", "Black", "White", "Cyan", "Gold"
        };

        SortedSet<String> tree = new TreeSet<>(Arrays.asList(colors));

        System.out.printf("sorted set: ");
        printSet(tree);

        // obtém headSet com base no 'Gold'
        System.out.print("headSet (\"Gold\"): ");
        printSet(tree.headSet("Gold"));

        // obtém tailSet com base no 'Black'
        System.out.print("tailSet (\"Black\"): ");
        printSet(tree.tailSet("Gold"));

        // obtém o primeiro e último elemento
        System.out.printf("first: %s%n", tree.first());
        System.out.printf("last: %s%n", tree.last());

    }

    private static void printSet(SortedSet<String> set) {
        for (String s : set) {
            System.out.printf("%s ", s);
        }
        System.out.println();
    }
}
    
