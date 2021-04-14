import java.util.Locale;

/**
 * stringTest1
 */
public class stringTest1 {

    public static void main(String[] args) {
        
        String first = "Test123";
        String second = "Test" + 123;

        boolean equals = first.equals(second);

        System.out.println("The strings is equals? "+equals);

        String firstString = "Test";
        String secondString = "TEST";

        boolean equalsIngnoreCase = firstString.equalsIgnoreCase(secondString);

        System.out.println("The strings is equals ignored case? "+equalsIngnoreCase);

        System.out.println("===================================================");

        String string1 = "Taki";
        String string2 = "TAKI";

        System.out.println("The strings is equals? "+string1.equalsIgnoreCase(string2));

        Locale locale = Locale.forLanguageTag("tr-TR");

        System.out.println( "The strings is equals in Turkish? "+string1.toLowerCase(locale).equals(string2.toLowerCase(locale)));

        Locale locale2 = Locale.forLanguageTag("fr-FR");
        System.out.println( "The strings is equals in Franch? "+string1.toLowerCase(locale2).equals(string2.toLowerCase(locale2)));
        

        String stringObj = new String("Brayen");
        String str = "Brayen";

        if (stringObj.equals(str)) {
            System.out.println("The strings are equal.");
        } 
        if (stringObj != str) {
            System.out.println("The strings aren't the same object.");
        }

        String internedString = stringObj.intern();

        if (internedString == str) {
            System.out.println("The interned string and the literal are the same object.");
        }
    }
}