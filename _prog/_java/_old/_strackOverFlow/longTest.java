import java.util.Objects;

/**
 * longTest
 */
public class longTest {

    public static void main(String[] args) {
        
        long high = Long.MAX_VALUE;
        long low = Long.MIN_VALUE;

        System.out.println("Long High value: "+high);
        System.out.println("Long Low value: "+low);

        System.out.println("==========================================");

        long var1 = 123L;
        long var2 = 123L;

        System.out.println("The values is equals? "+Objects.equals(var1, var2));
    
    }
}