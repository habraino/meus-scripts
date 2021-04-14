/**
 * Gerente
 */
public class Gerente extends Funcionario{

    private int senha;
    private int numGerente;

    @Override
    public double getBonus(){
        return this.salario * 0.15;
    }

    public boolean autentica(int senha)
    {
        if(this.senha == senha)
        {
            System.out.println("Acesso Permitido!");
            return true;
        }
        else
        {
            System.out.println("Acesso Negado!");
            return false;
        }
    }

    public int getSenha() {
        return senha;
    }

    public void setSenha(int senha) {
        this.senha = senha;
    }

    public int getNumGerente() {
        return numGerente;
    }

    public void setNumGerente(int numGerente) {
        this.numGerente = numGerente;
    }

}