/**
 * ControleDeBonus
 */
public class ControleDeBonus {

    private int totalBonus = 0;

    public void registra(Funcionario funcionario)
    {
        System.out.println("Adicionando bonificação do funcionario: " + funcionario);
        this.totalBonus += funcionario.getBonus();
    }

    public double getBonus(){
        return this.totalBonus;
    }
}
