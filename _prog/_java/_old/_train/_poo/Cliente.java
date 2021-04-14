/**
 * Cliente
 */
public class Cliente {

    protected String nome;
    protected int numBI;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getNumBI() {
        return numBI;
    }

    public void setNumBI(int numBI) {
        this.numBI = numBI;
    }

    @Override
    public String toString() {
        return "Cliente [nome=" + nome + ", numBI=" + numBI + "]";
    }
    
}