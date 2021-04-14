package caelum.poo;

public class Gerente extends Funcionario {

    private int senha;
    private int numeroDeFuncionariosGerenciados;


    public boolean autentica(int senha) {
        if (this.senha == senha) {
            System.out.println("Acesso permitido!");
            return true;
        } else {
            System.out.println("Acesso negado!");
            return false;
        }
    }

    @Override
    public double getBonificacao() {
        return super.getBonificacao() + 1000;
    }

}