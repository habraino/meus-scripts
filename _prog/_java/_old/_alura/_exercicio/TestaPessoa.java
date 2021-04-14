/**
 * TestaPessoa
 */
public class TestaPessoa {

    public static void main(String[] args) {
        Pessoa p = new Pessoa();

        p.nome = "Hebraino";
        p.idade = 20;

        System.out.println(p.nome);
        System.out.println(p.idade);
        p.fazerAniversario();
    }
}