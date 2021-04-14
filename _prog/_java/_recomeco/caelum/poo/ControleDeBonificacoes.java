package caelum.poo;

public class ControleDeBonificacoes {

    private double totalDeBonificacoes = 0;

    public void registra(Funcionario f) {
        System.out.println("Adicionando bonificação do funcionario: " + f.getClass());
        this.totalDeBonificacoes += f.getBonificacao();
    }

    public double getTotalDeBonificacoes() {
        return this.totalDeBonificacoes;
    }
    
}