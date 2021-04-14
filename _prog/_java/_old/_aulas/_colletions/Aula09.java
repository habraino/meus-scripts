import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Aula09
 */
public class Aula09 {

    public static void main(String[] args) {
        
        String[] colors = {
            "Green", "Red", "Blue", "Yellow", "Balck", "White", "Cyan", "Gold",
            "Silver", "Brown", "Violet", "Pink", "Purple", "Gray", "Orange",
            "Green", "Red", "Blue"
        };

        List<String> list = Arrays.asList(colors);

        System.out.printf("list: %s%n", list);

        // elimina as duplicatas
        printNotDuplicate(list);

    }

    private static void printNotDuplicate(Collection<String> values) {
        Set<String> set = new HashSet<>(values);

        System.out.printf("%nNonduplicates are: ");

        for (String value : set) {
            System.out.printf("%s ", value);
        }
        System.out.println();   
    }
}

