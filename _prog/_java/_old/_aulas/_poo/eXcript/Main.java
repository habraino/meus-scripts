/**
 * Main
 */
public class Main {

    public static void main(String[] args) {
        
        Mobile mobile;
        mobile = new Mobile();

        mobile.volume = 5;
        mobile.ligado = true;

        System.out.println("Ligado? "+mobile.ligado);
        System.out.println("Volume: "+mobile.volume);
    }
}