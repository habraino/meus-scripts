import java.util.Locale;

/**
 * stringTest2
 */
public class stringTest2 {

    public static void main(String[] args) {
        
        String string = "The Brayen is good programmer.";

        System.out.println("String: "+string);
        System.out.println("In Uppercase: "+string.toUpperCase());
        System.out.println("In LowerCase: "+string.toLowerCase());

        Locale locale = Locale.GERMANY;
        System.out.println(string.toLowerCase(locale).equalsIgnoreCase(string.toUpperCase(locale)));

    }
}