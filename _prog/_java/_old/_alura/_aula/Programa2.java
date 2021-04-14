/**
 * Programa2
 */
class Programa2 {

    public static void main(String[] args) {
        
        Conta c1 = new Conta();
        c1.deposita(200);

        Conta c2 = c1;
        c2.deposita(300);

        System.out.println(c1 == c2);

    }
    
}