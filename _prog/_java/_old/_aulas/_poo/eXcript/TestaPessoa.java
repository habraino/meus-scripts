
/**
 * TestaPessoa
 */
public class TestaPessoa {

    public static void main(String[] args) {

        int a = 1;
        
        while(a <= 5){
            System.out.printf("====== %dª Pessoa =======\n",a);
            Controler controler = new Controler();
            controler.pega();
            controler.obterTodos();
            a++;
        }
        
        
    }
}