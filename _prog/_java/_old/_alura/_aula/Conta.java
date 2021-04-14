/***
 * class Conta
 * file_name: Conta.java
 * date: 11-01-2020 at 18:31:50
 */

class Conta {

    // os atributos da classe Conta
    int numero;
    private double saldo;
    Cliente titular = new Cliente();

    // construtor
    Conta(){
        System.out.println("Construindo uma conta.");
    }

    // metodo para sacar alguma quantia
    public boolean saca(double quantidade)
    {
        if(this.saldo < quantidade)
        {
            return false;
        }else
        {
            double novoSaldo = this.saldo - quantidade;
            this.saldo = novoSaldo;
            return true;
        }
    }

    // metodo para depositar alguma quantia
    public void deposita(double quantia)
    {
        this.saldo += quantia;
    }

    // metodo para transferir alguma quantia para outra conta
    public boolean transfere(Conta destino, double valor)
    {
        boolean retirou = this.saca(valor);
        if(retirou == false)
        {
            return false;
        }
        else 
        {
            destino.deposita(valor);
            return true;
        }
    }
    // GETTERS E SETTERS
    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public Cliente getTitular() {
        return titular;
    }

    public void setTitular(Cliente titular) {
        this.titular = titular;
    }


}