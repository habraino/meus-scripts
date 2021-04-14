package caelum;

public class ValorExatoDePI {

    // método para achar o valor da raiz quadrada
    public static int sqrt(int a) {

        int x = 3; // minha 'constante'

        while (true) {
            int y = (x + a / x) / 2;
            if (x == y) {
                break;
            }
            x = y;
        }

        return x;
        
    }

    public static void main(String[] args) {
        
        int res = sqrt(9);
        System.out.println(res);

    }

}