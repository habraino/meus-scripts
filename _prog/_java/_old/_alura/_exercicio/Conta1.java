/**
 * Conta1
 */
public class Conta1 {

    String titular;
    int numero;
    double saldo;
    String agencia;
    String abertura;

    // saca dinheiro da conta
    boolean saca(double valor)
    {
        if(this.saldo < valor){
            return false;
        }else{
            this.saldo -= valor;
            return true;
        }
    }

    // deposita dinheiro na conta
    void deposita(double quantidade)
    {
        if(quantidade >= 0)
            this.saldo += quantidade;
    }

    // calcula rendimento mensal
    double rendimento()
    {
        return this.saldo * 0.1;
    }

    // imprime os dados
    String mostraTodos()
    {
        String dados = "Titular: " + this.titular;
        dados += "\nSaldo: " + this.saldo;
        dados += "\nRendimento: " + this.rendimento();
        return dados;
    }

}