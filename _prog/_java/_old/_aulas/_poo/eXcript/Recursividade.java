/**
 * Recursividade
 */

class Recursiva{

    // calcula fatorial de um num
    int fatorial(int n){
        if(n == 0){
            return 1;
        }
        return n * fatorial(n - 1);
    }

    // calcula a sequência de fibonacci
    int fibonacci(int n){
        if(n == 1){
            return 0;
        }
        else if(n == 2){
            return 1;
        }else{
            return fibonacci(n - 1) + fibonacci(n - 2);  
        }
    }
}
public class Recursividade {

    public static void main(String[] args) {
        
        Recursiva r = new Recursiva();

        System.out.println(r.fibonacci(8));
        System.out.println(r.fatorial(5));// mostra na tela 5!

    }
}