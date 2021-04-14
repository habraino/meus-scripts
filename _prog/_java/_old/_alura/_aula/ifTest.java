/**
 * ifTest
 */
public class ifTest {

    public static void main(String[] args) {
        
        boolean amigo = true;
        int idade = 16;

        if(idade < 18 && !amigo){
            System.out.println("Entrada concedida!!");
        }else{
            System.out.println("Não pode entrar!!");
        }

    }
}