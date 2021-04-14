/**
 * TestaPorta
 */
public class TestaPorta {

    public static void main(String[] args) {
        Porta porta = new Porta();

        porta.aberta = true;
        porta.cor = "Vermelha";
        porta.dimensaoX = 12;
        porta.dimensaoY = 25;
        porta.dimensaoZ = 5;

        // verifica condição da porta
        if(porta.aberta()){
            porta.fecha();
        }else{
            porta.abre();
        }

        System.out.println("Cor da porta: "+porta.cor);
    }
}