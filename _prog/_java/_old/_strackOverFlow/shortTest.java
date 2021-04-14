/**
 * shortTest
 */
public class shortTest {

    public static void main(String[] args) {
        
        short example = -37;
        short myShort = 96;
        short anotherShort = 7;

        short addedShorts = (short) (myShort + anotherShort);
        short subtractedShorts = (short) (myShort - anotherShort);

        System.out.println("Example: "+example);
        System.out.println("My short: "+myShort);
        System.out.println("Another short: "+anotherShort);
        System.out.println("Added shorts: "+addedShorts);
        System.out.println("Subtracted shorts: "+subtractedShorts);

        System.out.println("===========================================");

        short high = Short.MAX_VALUE;
        short low = Short.MIN_VALUE;

        System.out.println("High short value: "+high);
        System.out.println("Low short value: "+low);
    }
}