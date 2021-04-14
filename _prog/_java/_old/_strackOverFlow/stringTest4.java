import java.util.StringJoiner;
import java.util.StringTokenizer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * stringTest4
 */
public class stringTest4 {

    public static void main(String[] args) {
        
        String str1 = "Hello World";
        String str2 = "Hello";
        String str3 = "helLo";

        System.out.println(str1.contains(str2));
        System.out.println(str1.contains(str3));

        String line = "Brayen;Aida;30;3";
        String[] split = line.split(";");
        
        for (String string : split) {
            System.out.printf("%s ",string);
        }
        System.out.println();

        System.out.println("===================================");

        String s = "My name is Brayen Strong. And I study in High School Mé Xinhô.";
        StringTokenizer sTokenizer = new StringTokenizer(s);

        while (sTokenizer.hasMoreTokens()) {
            System.out.println(sTokenizer.nextToken());
        }

        System.out.println("=================================================");
        System.out.println("\t\tJoin Characters");
        System.out.println("=================================================");

        String[] elements = {"foo", "bar", "foobar"};
        String singleElement = String.join(" + ", elements);

        System.out.println(singleElement);

        System.out.println("=================================================");
        System.out.println("\t\tStringJoiner Test");
        System.out.println("=================================================");

        StringJoiner sj = new StringJoiner(", ", "[", "]");
        sj.add("foo");
        sj.add("bar");
        sj.add("foobar");

        System.out.println(sj);

        System.out.println("=================================================");
        System.out.println("\t\tJoining Colletor Test");
        System.out.println("=================================================");

        Stream<String> stringStream1 = Stream.of("foo", "bar", "foobar");
        Stream<String> stringStream2 = Stream.of("foo", "bar", "foobar");
        String joined1 = stringStream1.collect(Collectors.joining(", "));
        String joined2 = stringStream2.collect(Collectors.joining(", ", "{", "}"));

        System.out.println("Joined: "+joined1);
        System.out.println("Joined: "+joined2);

    }
}