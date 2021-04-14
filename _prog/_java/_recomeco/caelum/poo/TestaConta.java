package caelum.poo;

public class TestaConta {

    public static void main(String[] args) {

        Conta c1 = new Conta();
        c1.deposita(200);

        Conta c2 = c1; // linha importante!
        c2.deposita(100);

        System.out.println(c1 == c2);

    }

}