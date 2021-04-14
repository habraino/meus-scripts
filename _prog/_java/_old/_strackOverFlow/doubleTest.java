/**
 * doubleTest
 */
public class doubleTest {

    public static void main(String[] args) {
        
        double high = Double.MAX_VALUE;
        double low = Double.MIN_VALUE;

        System.out.println(high);
        System.out.println(low);

        double notationScientific = 1.2e-3;
        System.out.println("ScientificNotation: "+notationScientific);

        System.out.println("================================");

        double d1 = 0d;
        double d2 = -0d;

        System.out.println(d1 == d2);
        System.out.println(1d / d1);
        System.out.println(1d / d2);
    }
}