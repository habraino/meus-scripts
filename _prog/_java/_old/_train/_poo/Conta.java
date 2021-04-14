/**
 * Conta
 */
public class Conta extends Cliente{

    public String titular;
    private double saldo;
    public double limite;
    protected Cliente cliente = new Cliente();

    public boolean depositarEm(double valor){
        if(valor >= 0){
            this.saldo += valor;
            return true;
        }
        return false;
    }

    public boolean sacarDinheiro(double valor){
        if( valor <= 0 || valor > this.saldo )
            return false;
        else
            this.saldo -= valor;
            return true;
    }

    public boolean tresferirPara(double valor, Conta destino){
        if(valor > this.saldo){
            return false;
        }
        destino.saldo += valor;
        this.saldo -= valor;
        return true;
    }

    @Override
    public String toString() {
        return "Conta [limite=" + limite + ", saldo=" + saldo + ", titular=" + titular + "]";
    }

    
}