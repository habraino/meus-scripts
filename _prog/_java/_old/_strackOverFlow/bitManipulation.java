/**
 * bitManipulation
 */
public class bitManipulation {

    private static final long first_bit = 1L << 0;
    private static final long second_bit = 2L << 1;
    private static final long third_bit = 3L << 2;
    private static final long fourth_bit = 4L << 3;
    private static final long fifth_bit = 5L << 4;
    private static final long bit_55 = 1L << 54;

    public static void checkBitMask(long checkBitMask) {
        System.out.println("FIRST_BIT: "+((checkBitMask & first_bit) != 0));
        System.out.println("SECOND_BIT: "+((checkBitMask & second_bit) != 0));
        System.out.println("THIRD_BIT: "+((checkBitMask & third_bit) != 0));
        System.out.println("FOURTH_BIT: "+((checkBitMask & fourth_bit) != 0));
        System.out.println("FIFTH_BIT: "+((checkBitMask & fifth_bit) != 0));
        System.out.println("BIT_55: "+((checkBitMask & bit_55) != 0));
    }

    public static void main(String[] args) {
        
        checkBitMask(first_bit | third_bit | fifth_bit | bit_55);

    }
}