/**
 * floatTest
 */
public class floatTest {

    public static void main(String[] args) {
        
        float f1 = 0f;
        float f2 = -0f;

        System.out.println(f1 == f2);   
        System.out.println(1f / f1);
        System.out.println(1f / f2);

        float high = Integer.MAX_VALUE;
        float low = Integer.MIN_VALUE;

        System.out.println(high);
        System.out.println(low);
    }
}