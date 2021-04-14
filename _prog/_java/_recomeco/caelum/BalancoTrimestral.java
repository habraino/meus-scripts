package caelum;

public class BalancoTrimestral {

    public static void main(String[] args) {
        
        int gastosJaneiro = 15000;
        int gastosFevereiro = 23000;
        int gastosMarco = 17000;

        int gastosTrimestre = gastosJaneiro + gastosFevereiro + gastosMarco;
        double mediaMensal = gastosTrimestre / 3;

        System.out.println("O gasto trimestral é de: "+gastosTrimestre);
        System.out.println("A média mensal é: "+mediaMensal);

    }

}