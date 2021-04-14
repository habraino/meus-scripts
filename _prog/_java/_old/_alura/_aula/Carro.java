/**
 * Carro
 */
public class Carro {

    String cor;
    String modelo;
    double velAtual;
    double velMax;

    // liga o carro
    void liga()
    {
        System.out.println("O carro está ligado.");
    }

    // acelera a uma quantidade
    void acelera(double quantidade)
    {
        double novaVelocidade = this.velAtual + quantidade;
        this.velAtual += novaVelocidade;
    }

    // devolve a marcha do carro
    int marcha()
    {
        if(this.velAtual < 0){
            return -1;
        }
        if(this.velAtual >= 0 && this.velAtual < 40){
            return 1;
        }
        if(this.velAtual >= 40 && this.velAtual < 80){
            return 2;
        }
        return 3;
    }

}