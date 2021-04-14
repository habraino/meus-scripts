/**
 * Construtor
 */

class Janela{

    int altura, largura;

    Janela(int altura, int largura){
        this.altura = altura;
        this.largura = largura;
    }
    Janela(){
        this(150, 200);
    }

    void imprime(){
        System.out.println("A Altura = "+altura+", a largura = "+largura);
    }
}

public class Construtor {

    public static void main(String[] args) {
        new Janela(250, 300).imprime();
        new Janela().imprime();
    }
}
