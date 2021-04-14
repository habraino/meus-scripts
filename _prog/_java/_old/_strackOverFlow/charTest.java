/**
 * charTest
 */
public class charTest {

    public static void main(String[] args) {
        
        char heart = '\u2764';
        System.out.println(heart);

        /*
        for (char i = 0; i <= 9000; i++) {
            System.out.printf("%c",i);
        }*/

        /*int a = (char) '⌚';
        int b = (char) '⌛';
        System.out.println(a);
        System.out.println(b);*/

        for (int i = 0; i < 26; ++i) {
            char letter = (char) ('A' + i);
            System.out.print(letter);
        }
        System.out.println();

    }
}