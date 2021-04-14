/**
 * byteTest
 */
public class byteTest {

    public static void main(String[] args) {
        
        byte high = Byte.MAX_VALUE;
        byte low = Byte.MIN_VALUE;

        System.out.println("Byte High Value: "+high);
        System.out.println("Byte Low Value: "+low);

        byte example = -37;
        byte myByte = 96;
        byte anotherByte = 7;

        byte addedBytes = (byte) (myByte + anotherByte);
        byte subtractedBytes = (byte) (myByte - anotherByte);

        System.out.println("Example: "+example);
        System.out.println("My byte: "+myByte);
        System.out.println("Another byte: "+anotherByte);
        System.out.println("AddedBytes: "+addedBytes);
        System.out.println("SubtractedBytes: "+subtractedBytes);
        
    }
}