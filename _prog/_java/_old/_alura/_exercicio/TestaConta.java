/**
 * TestaConta
 */
public class TestaConta {

    public static void main(String[] args) {
        
        Conta1 minhaConta = new Conta1();

        minhaConta.titular = "Brayen";
        minhaConta.numero = 12345;
        minhaConta.saldo = 1200;
        minhaConta.agencia = "BISTP";
        minhaConta.abertura = "11-01-2020";

        minhaConta.deposita(5065);

        System.out.println(minhaConta.mostraTodos());        

    }
}