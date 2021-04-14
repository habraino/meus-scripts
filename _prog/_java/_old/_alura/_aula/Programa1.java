/**
 * Programa
 */
class Programa {

    public static void main(String[] args) {
        Conta minhaConta = new Conta();

        // alterando os valores dos atributos da conta
        minhaConta.titular.setNome("Brayen");
        minhaConta.setSaldo(2300.0);

        // imprime o saldo atual
        System.out.printf("O saldo atual do %s é de: %.2f\n",minhaConta.titular.getNome(),    minhaConta.getSaldo());

        // saca uma 300€ na conta
        boolean consegui = minhaConta.saca(300);

        if(consegui)
        {
            System.out.println("Consegui sacar!");
        }
        else 
        {
            System.out.println("Não consegui sacar!");
        }

        // imprime novo saldo depois de sacar 200€
        System.out.printf("Novo saldo depois do saque: %.2f\n",minhaConta.getSaldo());

        // deposita 500€ na conta
        minhaConta.deposita(500);

        // imprime novo saldo depois de depositar 500€
        System.out.printf("Novo saldo depois do deposito: %.2f\n",minhaConta.getSaldo());
    }
    
}