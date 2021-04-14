/**
 * objectCasting
 */
public class objectCasting {

    public static void main(String[] args) {
        
        Float floatVar1 = new Float(42.0f);
        Number n = floatVar1;
        Float floatVar2 = (Float) n;
        Double doubleVar = (Double) n;

        System.out.println(floatVar1);
        System.out.println(n);
        System.out.println(floatVar2);
        System.out.println(doubleVar);

    }
}