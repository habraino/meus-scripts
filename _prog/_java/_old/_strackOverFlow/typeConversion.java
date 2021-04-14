/**
 * typeConversion
 * @see <a href="https://www.google.com.br"> Google </a>
 */
public class typeConversion {

    public static void main(String[] args) {
        
        char charVar1 = (char) 65;
        byte byteVar1 = (byte) 'A';
        short shortVar1 = (short) 'A';
        int intVar1 = (int) 'A';

        System.out.println(charVar1);
        System.out.println(byteVar1);
        System.out.println(shortVar1);
        System.out.println(intVar1);

        System.out.println("=========================================");

        char charVar2 = (char) 8253;
        byte byteVar2 = (byte) '‽';
        short shortVar2 = (short) '‽';
        int intVar2 = (int) '‽';

        System.out.println(charVar2);
        System.out.println(byteVar2);
        System.out.println(shortVar2);
        System.out.println(intVar2);

    }
}