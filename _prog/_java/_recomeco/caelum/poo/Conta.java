package caelum.poo;

public class Conta {
    
    private int numero = 1234;
    Cliente titular;
    private double saldo = 1000.0; 

    private static int totalDeContas;

    public Conta(){
        Conta.totalDeContas += 1;
    }

    boolean saca(double quantidade) {
        if (this.saldo < quantidade) {
            return false;
        } else {
            this.saldo -= quantidade;
            return true;
        }
    }

    void deposita(double quantidade) {
        this.saldo += quantidade;
    }

    boolean transferePara(Conta destino, double valor) {
        boolean retirou = this.saca(valor);
        if (retirou == false) {
            return false; // não deu para sacar
        } else {
            destino.deposita(valor);
            return true;
        }
    }

    public static int getTotalcontas() {
        return Conta.totalDeContas;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    


}

