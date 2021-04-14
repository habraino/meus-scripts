/**
 * Argumento_Parm
 */

/**
 * Calculo
 */
class Calculo {

    public void soma(int arg1, int arg2){
        System.out.println("A soma é: "+(arg1+arg2));
    }
    
}
public class Argumento_Parm {

    public static void main(String[] args) {
        
        Calculo cal = new Calculo();
        cal.soma(12, 5);
        
    }
}