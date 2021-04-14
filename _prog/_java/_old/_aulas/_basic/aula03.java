// programa que exemplifica a operador ternária

public class aula03 {

    public static void main(String[] args) {
        
        int a, b;
        String valor;

        a = 5; 
        b = 10;

        /** 
        if (a < b)
            valor = "Verdadeiro";
        else
            valor = "Falso";
        */

        // mesma coisa que a condição em cima
        valor = (a < b) ? "Verdadeiro" : "Falso";
        System.out.println(valor);

    }

}