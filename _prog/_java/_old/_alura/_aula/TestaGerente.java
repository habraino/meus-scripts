/**
 * TestaGerente
 */
public class TestaGerente {

    public static void main(String[] args) {
        
        ControleDeBonus controleDeBonus = new ControleDeBonus();
        Gerente funcionario1 = new Gerente();
        Funcionario funcionario2 = new Funcionario();


        funcionario1.nome = "Hugo";
        funcionario1.setSenha(1234);
        funcionario1.autentica(1234);

        funcionario1.setSalario(5000);
        controleDeBonus.registra(funcionario1);

        funcionario2.setSalario(1000);
        controleDeBonus.registra(funcionario2);


        System.out.println(controleDeBonus.getBonus());

    }
}