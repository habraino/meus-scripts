import java.util.StringTokenizer;

/**
 * stringTest9
 */
public class stringTest9 {

    public static void main(String[] args) {
        
        StringTokenizer sTokenizer = new StringTokenizer("brayen strong bom é um bom programador", " ");

        while (sTokenizer.hasMoreTokens()) {
            System.out.println(sTokenizer.nextToken());
        }

    }
}