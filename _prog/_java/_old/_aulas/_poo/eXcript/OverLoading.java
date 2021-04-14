/**
 * OverLoading
 */

 /*
 * fazendo sobreCarga nas funções, ou seja usar mesmo 
 * nome da função para finalidade diferente!!
 * */
class SobreCarga{
    // imprime "A soma é:"
    void soma(int x, int y){
        int s = x + y;
        System.out.println("A soma é: "+s);
    }

    // retorna true se x for igual a 20 senão retorna false
    boolean soma(int x){
        return x == 20 ? true : false;
    }

    // mostra o resultado da soma na tela
    int soma(int a, int b, int c){
        System.out.println(a+b+c);
        return 1;
    }
}

public class OverLoading {

    public static void main(String[] args) {
        // cria nova instância da classe SobreCarga()
        SobreCarga s = new SobreCarga();
        s.soma(20, 1, 30);
        System.out.println(s.soma(20));
        s.soma(20, 10);
    }
}