
/**
 * TestaInterface
 */
public class TestaInterface {

    public interface Calculo{
        int getSoma();
    }

    /**
     * Testa
     */
    public interface Testa {
    
        boolean teste(int x);
    }

    public static void main(String[] args) {
        
        Calculo c;
        int soma = 12 + 34;
        c = () -> soma;
        System.out.println(c.getSoma());


        Testa isPar;
        isPar = (int y) -> (y % 2 == 0);
        System.out.println(isPar.teste(2018));
        
    }
}
