/**
 * TestaConta
 */
public class TestaConta extends Conta{

    public static void main(String[] args) {
        
        Conta c1 = new Conta();

        c1.cliente.nome = "Brayen Strong";

        c1.titular = c1.cliente.nome;
        c1.limite = 12000;
        c1.depositarEm(4000);

        System.out.println(c1.toString());

    }
}