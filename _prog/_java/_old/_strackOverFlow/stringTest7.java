import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * stringTest7
 */

public class stringTest7 {

    public static int countStringInString(String search, String text) {
        Pattern pattern = Pattern.compile(search);
        Matcher matcher = pattern.matcher(text);

        int cont = 0;
        while (matcher.find()) {
            cont++;
        }
        return cont;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter to text: ");
        String text = scanner.nextLine();

        System.out.println(countStringInString("a", text));
        System.out.println(countStringInString(",", text));

        scanner.close();
    }
}