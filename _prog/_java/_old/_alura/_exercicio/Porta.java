/**
 * Porta
 */
public class Porta {

    boolean aberta;
    String cor;
    int dimensaoX;
    int dimensaoY;
    int dimensaoZ;

    public void abre(){
        System.out.println("Porta aberta");
    }

    public void fecha(){
        System.out.println("Porta fechada");
    }

    public boolean aberta(){
        if (this.aberta == true){
            return true;
        }else{
            return false;
        }
    }
}