/**
 * Aula02
 */
public class Aula02 {

    interface Num{
        int getValue();
    }

    interface Numeric{
        boolean teste(int x);
    }

    interface Div{
        boolean teste2(int x, int y);
    }

    public static void main(String[] args) {
        
        Num n;
        int soma = 12 - 5;
        n = () -> soma;
        System.out.println(n.getValue());

        Numeric isPar = (int x) -> (x % 2 == 0);
        System.out.println(isPar.teste(89));
        System.out.println(isPar.teste(90));

        Div p = (x, y) -> x % y == 0;
        System.out.println(p.teste2(12, 2));

    }
}