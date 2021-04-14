import java.util.List;
import java.util.Arrays;
import java.util.Collections;

/**
 * Aula03
 */
public class Aula03 {

    public static void main(String[] args) {
        String[] cities = {"London", "New York", "Neves", "Lisbon"};
        List<String> list = Arrays.asList(cities);
        System.out.println("Unsorted list:");
        System.out.printf("%s %n%n", list);
        
        Collections.sort(list);
        System.out.println("Sorted list:");
        System.out.printf("%s %n%n", list);

        Collections.sort(list, Collections.reverseOrder());
        System.out.println("Sorted list:");
        System.out.printf("%s %n%n", list);

    }

}