/**
 * Cliente
 */
class Cliente {

    private String nome;
    private String sobreNome;
    private String cpf;
    private int idade;

    public void mudaCPF(String cpf)
    {
        if(this.idade <= 60){
            validaCPF(cpf);
        }
        this.cpf = cpf;
    }

    public void validaCPF(String cpf)
    {

    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobreNome() {
        return sobreNome;
    }

    public void setSobreNome(String sobreNome) {
        this.sobreNome = sobreNome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

}