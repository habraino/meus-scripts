package caelum.poo;

public class Cliente {

    private String nome;
    private String sobreNome;
    private String cpf;
    private int idade;

    public void mudaCPF(String cpf) {
        if (this.idade <= 60) {
            validaCPF(cpf);
        }
        this.cpf = cpf;
    }

    public void validaCPF(String cpf) {
        
    }
} 