/**
 * TestaCarro
 */
public class TestaCarro {

    public static void main(String[] args) {
        
        Carro meuCarro = new Carro();

        meuCarro.cor = "Branco e Preto";
        meuCarro.modelo = "MacLaren";
        meuCarro.velAtual = 0;
        meuCarro.velMax = 80;

        // liga o carro
        meuCarro.liga();

        // acelera até 20km/h
        meuCarro.acelera(20);

        System.out.println(meuCarro.velAtual);

    }
}