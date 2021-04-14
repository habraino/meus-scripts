
/**
 * FibonacciSequency
 */
public class FibonacciSequency {

    public static void main(String[] args) {
        Fibonacci fibonacci = new Fibonacci();

        System.out.print("[");
        for(int i = 1; i <= 10; i++){
            System.out.print(" "+fibonacci.calculaFibo2(i));
        }
        System.out.println(" ]");
    }
}
